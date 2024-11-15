import numpy as np
import pandas as pd
from pymongo import MongoClient


from database import MongoConnector
from utils import get_full_fake
import os


class ResponseService:

    def __init__(self):

        self.mongo_address = os.getenv("MONGO_ADDRESS")
        self.db_connector = MongoConnector(self.mongo_address)
        self.mongo_clinet = MongoClient(os.getenv('MONGO_ADDRESS'))
        self._load_collection()
        self.datetime_format = '%Y-%m-%d'
        self.full_fake = get_full_fake(path='./docs/fake_data.yaml')
        self.fake_gen = get_full_fake(path='./docs/fake_gen.yaml')

    def _load_collection(self):
        
        name = 'company'
        collection = 'twse_stats'
        self.collection = self.db_connector.point_collection(
            name = name,
            collection = collection
        )
        
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