import datetime

from database import MongoConnector
from utils import StatsFetcher, get_full_fake

class ResponseService:

    def __init__(self):
        self.mongo_address = "mongodb://neurowatt:neurodb123@db.neurowatt.ai:27017/neurowatt"
        self.db_connector = MongoConnector(self.mongo_address)
        self._load_collection()
        self.data_fetcher = StatsFetcher()
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