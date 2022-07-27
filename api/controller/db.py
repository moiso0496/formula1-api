from pymongo import MongoClient

class DatabaseClient:
    def __init__(self, host, database) -> None:
        self.client = MongoClient(host)
        self.collection = None
        self.db = self.client[database]

    def create_document(self, _doc):
        res = self.collection.insert_one(_doc)
        return res
    
    def update_document(self,_update_query, _update_dict):
        res = self.collection(_update_query, _update_dict)
        return res

    def get_document(self,_search_query):
        res = self.collection.find_one(_search_query,{"_id" : 0})
        return res
    
    def delete_document(self,_delete_query):
        res = self.collection.delete_one(_delete_query)
        return res



    
