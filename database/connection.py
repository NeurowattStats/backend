from pymongo import MongoClient
import redis
from dotenv import load_dotenv
import os
import openai
from pymilvus import MilvusClient
from llama_index.core import VectorStoreIndex
from llama_index.vector_stores.milvus import MilvusVectorStore

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


class MilvusConnector(DatabaseConnector):

    def __init__(self, address: str, token: str):
        super().__init__(address)
        self.token = token
        self.client = MilvusClient(uri=self.address, token=self.token)

    def point_collection(self, collection: str) -> None:
        """
        指定Milvus的collection
        """
        self.vector_store = MilvusVectorStore(uri=self.address,
                                              token=self.token,
                                              collection_name=collection,
                                              overwrite=False,
                                              similarity_metric='cosine')

        return self.vector_store

    def load_vector_store(self, collection: str) -> None:
        """
        輸入RAG需要的index (輸入DB中所有index)
        """
        self.point_collection(collection=collection)
        self.index = VectorStoreIndex.from_vector_store(self.vector_store)

        return self.index


class RedisConnector(DatabaseConnector):

    def __init__(self, host: str, port: int, password: str):
        super().__init__(f"{host}:{port}")
        self.client = redis.StrictRedis(host=host,
                                        port=port,
                                        password=password,
                                        decode_responses=True)

    def get(self, key: str):
        return self.client.get(key)

    def set(self, key: str, value: str):
        return self.client.set(key, value)

    def delete(self, key: str):
        return self.client.delete(key)


# Initialize Redis connection
redis_connector = RedisConnector(host=os.getenv("REDIS_ADDRESS",
                                                "default_address"),
                                 port=6379,
                                 password=os.getenv("REDIS_PASSWORD",
                                                    "default_pwd"))
