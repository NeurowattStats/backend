from pymongo import MongoClient

class DatabaseConnector:

    def __init__(self, address):
        self.address = address

class MongoConnector(DatabaseConnector):

    def __init__(self, address:str):
        super().__init__(address)

        self.client = MongoClient(
            self.address
        )

    def point_collection(self, name:str, collection:str)->None:
        
        self.db = self.client[name]
        self.collection = self.db[collection]

        return self.db[collection]

    