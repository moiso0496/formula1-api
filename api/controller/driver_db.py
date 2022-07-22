from api.controller.db import DatabaseClient

class DriverDataBase(DatabaseClient):
    def __init__(self, host) -> None:
        super().__init__(host, "drivers")
        self.collection = self.db["drivers"]
    
