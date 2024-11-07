import pandas as pd
import numpy as np
from collections.abc import Iterable
from database import MongoConnector
from utils import StatsFetcher, get_full_fake

class ResponseService:
    """
    Base service class providing common methods and properties for financial data handling.
    """

    def __init__(self, mongo_address=None):
        """
        Initialize the response service with MongoDB connection and data fetcher.
        """
        self.mongo_address = mongo_address or "mongodb://neurowatt:neurodb123@db.neurowatt.ai:27017/neurowatt"
        self.db_connector = MongoConnector(self.mongo_address)
        self.data_fetcher = StatsFetcher()
        self.datetime_format = '%Y-%m-%d'
        self.full_fake = get_full_fake(path='./docs/fake_data.yaml')
        self.fake_gen = get_full_fake(path='./docs/fake_gen.yaml')
        self.collection = self._load_collection()

    def _load_collection(self, name='company', collection='twse_stats'):
        """
        Load the specified MongoDB collection.
        """
        return self.db_connector.point_collection(name=name, collection=collection)

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
            return data.applymap(lambda x: marker if is_empty(x) else x)
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
