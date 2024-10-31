import datetime

from database import MongoConnector
from utils import query_data, get_full_fake

class ResponseService:

    def __init__(self):
        self.mongo_address = "mongodb://neurowatt:neurodb123@db.neurowatt.ai:27017/neurowatt"
        self.db_connector = MongoConnector(self.mongo_address)
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

    def query_full_data(self, ticker:str, start_date:datetime.datetime, end_date:datetime.datetime):

        """
        Fetches the full data for a specified ticker and date range.

        Args:
            ticker (str): The stock ticker symbol.
            start_date (datetime): The start date for data fetching.
            end_date (datetime): The end date for data fetching.

        Returns:
            pd.DataFrame: The fetched data as a DataFrame.
        """

        return query_data(
            ticker = ticker,
            start_date = start_date,
            end_date = end_date
        )
