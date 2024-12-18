from pymongo import MongoClient
import redis
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class DatabaseConnector:

    def __init__(self, address):
        self.address = address

class MongoConnector(DatabaseConnector):

    def __init__(self, address: str):
        super().__init__(address)
        self.client = MongoClient(self.address)

    def point_collection(self, name: str, collection: str) -> None:
        self.db = self.client[name]
        self.collection = self.db[collection]
        return self.db[collection]

class RedisConnector(DatabaseConnector):

    def __init__(self, host: str, port: int, password: str):
        super().__init__(f"{host}:{port}")
        self.client = redis.StrictRedis(
            host=host,
            port=port,
            password=password,
            decode_responses=True
        )

    def get(self, key: str):
        return self.client.get(key)

    def set(self, key: str, value: str):
        return self.client.set(key, value)

    def delete(self, key: str):
        return self.client.delete(key)

# Initialize Redis connection
redis_connector = RedisConnector(
    host=os.getenv("REDIS_ADDRESS", "default_address"),
    port=6379,
    password=os.getenv("REDIS_PASSWORD", "default_pwd")
)
