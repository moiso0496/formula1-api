from sqlite3 import connect
from pymongo import MongoClient

class DatabaseClient:
    def __init__(self, host, database) -> None:
        self.client = MongoClient(host)
        self.db = self.client[database]
        


    
