from pymongo import MongoClient

class DatabaseClient:
    def __init__(self, host, database) -> None:
        self.client = MongoClient(host)
        self.collection = None
        self.db = self.client[database]

    def create_document(self, _doc):
        self.collection.insert_one(_doc)
    
    def update_document(self,_update_query, _update_dict):
        self.collection(_update_query, _update_dict)
        

    def get_document(self,_search_query):
        self.collection(_search_query)
    
    def delete_document(self,_delete_query):
        self.collection.delete_one(_delete_query)
        



    
