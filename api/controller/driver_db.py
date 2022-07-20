from db import DatabaseClient

class DriverDataBase(DatabaseClient):
    def __init__(self, host) -> None:
        super().__init__(host)
    
    def create_access_driver_collection(self):
        self.collection = self.db["drivers"]
    
    def create_document(self):
        pass
    
    def update_document(self):
        pass

    def get_document(self):
        pass
    
    def delete_document(self):
        pass
