import numpy as np
import pandas as pd
from pymongo import MongoClient
from database import MongoConnector, MongoHelper
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
        self.query_helper = MongoHelper()
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
    
    def get_latest_generation(self, category: str) -> str:
        """
        查詢最新的指定 category 的 generation。

        :param category: 要查詢的 category
        :return: 最新的 generation 或 '不適用' (如未找到)
        """
        try:
            result = self.query_helper.find_the_lastest(
                collection=self.content_collection,  # 修正為 content_collection
                query={"category": category}
            )
            
            if result:
                return result.get("generation", "不適用")  # 如果 generation 缺失，返回默認值
            else:
                print(f"No document found for category: {category}")
                return "不適用"  # 未找到匹配的文檔
            
        except Exception as e:
            print(f"Error fetching latest generation for category {category}: {e}")
            return "不適用"  # 出現錯誤時返回默認值
            
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
            title_dict.update({f'{index}': f'{value}' for index, value in zip(indexes, non_index_df[col])})  # 使用 zip 和 dict 更新字典
            result.append(title_dict)

        return result

    @staticmethod
    def format_dict_values(data: dict, decimal_places: int = 2) -> dict:
        """
        格式化字典中的 float 值，保留指定的小數位數。

        :param data: 要處理的字典
        :param decimal_places: 小數點位數，默認為 2
        :return: 格式化後的字典
        """
        formatted_dict = {}

        for key, value in data.items():
            if isinstance(value, float):
                # 將 float 格式化為指定的小數位數
                formatted_dict[key] = round(value, decimal_places)
            elif isinstance(value, dict):
                # 如果值是嵌套字典，遞歸格式化
                formatted_dict[key] = ResponseService.format_dict_values(value, decimal_places)
            else:
                # 其他類型保持原樣
                formatted_dict[key] = value

        return formatted_dict
    
    @staticmethod
    def float_to_percentage(value: float, decimal_places: int = 2) -> str:
        """
        将单个 float 值转换为百分比格式的字符串。

        :param value: 要处理的浮点数
        :param decimal_places: 小数点位数，默认 2
        :return: 格式化为百分比的字符串
        """
        if not isinstance(value, float):
            raise ValueError("The value must be a float.")
        
        return f"{value * 100:.{decimal_places}f}%"
        
    @staticmethod
    def format_value_to_percentage(data: dict, keys: list, decimal_places: int = 2) -> dict:
        """
        将指定 key 对应的值通过 float_to_percentage 转换为百分比格式。

        :param data: 包含数据的字典
        :param keys: 需要转换的 key 列表
        :param decimal_places: 小数点位数，默认 2
        :return: 转换后的字典
        """
        formatted_data = {}
        for key, value in data.items():
            if key in keys and isinstance(value, (float, int)):
                formatted_data[key] = ResponseService.float_to_percentage(value, decimal_places)
            else:
                formatted_data[key] = value
        return ResponseService.format_dict_values(formatted_data)
    
    @staticmethod
    def format_values_within_range_to_percentage(
        data: dict, 
        keys: list = None, 
        upper_limit: float = 1.0, 
        lower_limit: float = -1.0, 
        decimal_places: int = 2
    ) -> dict:
        """
        将字典中指定范围 (lower_limit, upper_limit] 内的数值转换为百分比格式。

        :param data: 包含数据的字典
        :param keys: 需要转换的 key 列表，默认为 None。如果为 None，则处理整个字典。
        :param upper_limit: 上限（包含），默认为 1.0,。
        :param lower_limit: 下限（不包含），默认为 -1.0。
        :param decimal_places: 小数点位数，默认 2。
        :return: 转换后的字典。
        """
        formatted_data = {}

        # 如果 keys 为 None，处理整个字典
        keys_to_process = keys if keys is not None else data.keys()

        for key, value in data.items():
            if key in keys_to_process and isinstance(value, (float, int)):
                # 如果值在范围内，转换为百分比
                if lower_limit < value <= upper_limit:
                    formatted_data[key] = ResponseService.float_to_percentage(value, decimal_places)
                else:
                    formatted_data[key] = value  # 不在范围内的值保持不变
            else:
                formatted_data[key] = value  # 非指定 key 或非数值保持不变

        return ResponseService.format_dict_values(formatted_data)
