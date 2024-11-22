import numpy as np
import pandas as pd
from pymongo import MongoClient
from database import MongoConnector
from utils import get_full_fake
import os

class ResponseService:
    """
    Base service class providing common methods and properties for financial data handling.
    """

    def __init__(self):

        self.mongo_address = os.getenv("MONGO_ADDRESS")
        self.db_connector = MongoConnector(self.mongo_address)
        self.mongo_clinet = MongoClient(os.getenv('MONGO_ADDRESS'))
        self.datetime_format = '%Y-%m-%d'
        self.full_fake = get_full_fake(path='./docs/fake_data.yaml')
        self.fake_gen = get_full_fake(path='./docs/fake_gen.yaml')

        self.collection = self._load_collection(
            name = 'company',
            collection = 'twse_stats'
        )
        self.content_collection = self._load_collection(
            name = 'content_generation',
            collection = 'stats'
        )

    def _load_collection(
            self, 
            name:str, 
            collection:str
        ):
        
        return self.db_connector.point_collection(
            name = name,
            collection = collection
        )

    def _get_data(self, data: dict, key: str, default='不適用'):
        """Retrieve data with a key from the given data structure and handle missing values."""
        return data.get(key, default)

    def _get_multiple_data(self, data: dict, fields: list) -> dict:
        """Helper method to retrieve multiple fields from seasonal data."""
        return {field: self._get_data(data, field) for field in fields}
    
    def _get_title_array_from_full_page(self, full_page:dict, key: str):
        """
        通用方法：根據鍵提取資料並轉換為標題數組格式
        :param key: 欲提取的資料鍵（如 'month_revenue', 'this_month_revenue_over_years', 'grand_total_over_years' 等）
        :return: TitleArray 實例
        """
        data = self._get_data(full_page, key).reset_index()
        array = ResponseService.df_to_title_array(
            df=data,
            index_col='index',
            empty_values='不適用'
        )
        return array
        
    @staticmethod
    def replace_empty_values(data, marker):
        """
        Recursively replace None, NaN, and other empty-like values with a specified marker in various data types.
        """
        # 檢查空值
        def is_empty(x):
            return x is None or (isinstance(x, float) and np.isnan(x))

        # 處理不同資料型態
        if isinstance(data, pd.DataFrame):
            return data.map(lambda x: marker if is_empty(x) else x)
        elif isinstance(data, pd.Series):
            return data.apply(lambda x: marker if is_empty(x) else x)
        elif isinstance(data, dict):
            return {k: ResponseService.replace_empty_values(v, marker)
                    if isinstance(v, (dict, list, tuple, set, pd.Series, pd.DataFrame))
                    else (marker if is_empty(v) else v)
                    for k, v in data.items()}
        elif isinstance(data, list):
            return [ResponseService.replace_empty_values(x, marker)
                    if isinstance(x, (dict, list, tuple, set, pd.Series, pd.DataFrame))
                    else (marker if is_empty(x) else x)
                    for x in data]
        elif isinstance(data, tuple):
            return tuple(ResponseService.replace_empty_values(list(data), marker))
        elif isinstance(data, set):
            return {ResponseService.replace_empty_values(x, marker)
                    if isinstance(x, (dict, list, tuple, set, pd.Series, pd.DataFrame))
                    else (marker if is_empty(x) else x)
                    for x in data}
        else:
            return marker if is_empty(data) else data
        
    @staticmethod
    def df_to_title_array(
        df: pd.DataFrame, 
        index_col: str, 
        empty_values: str = '不適用'
    ) -> list: 

        # 替換空值
        replaced_df = ResponseService.replace_empty_values(
            data=df,
            marker=empty_values
        )

        # 提取索引列
        indexes = replaced_df[index_col].tolist()

        # 去除索引列
        try:
            non_index_df = replaced_df.drop(index_col, axis=1)
        except:
            non_index_df = replaced_df

        result = []

        # 遍歷非索引列
        for col in non_index_df.columns:
            title_dict = {'title': col}  # 初始化字典
            title_dict.update({index: value for index, value in zip(indexes, non_index_df[col])})  # 使用 zip 和 dict 更新字典
            result.append(title_dict)

        return result

    