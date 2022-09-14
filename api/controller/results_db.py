from api.controller.db import DatabaseClient


class ResultsDataBase(DatabaseClient):
    def __init__(self, host) -> None:
        super().__init__(host, "fsd-formula1")
        self.collection = self.db["results"]
    