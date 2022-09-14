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
        res = self.collection.update_one(_update_query, {"$set":_update_dict})
        return res

    def get_one_document_with_filter_values(self,_search_query, filter_values = {}):
        filter_values["_id"] = 0
        res = self.collection.find_one(_search_query, filter_values )
        return res

    def get_all_documents(self, filter_values={}):
        filter_values["_id"] = 0
        res = self.collection.find({}, filter_values)
        return list(res)
    
    def get_documents_with_filter_values(self, _search_query, filter_values):
        filter_values["_id"] = 0
        res = self.collection.find_one(_search_query, filter_values )
        return res

    

    
    def delete_document(self,_delete_query):
        res = self.collection.delete_one(_delete_query)
        return res



    
