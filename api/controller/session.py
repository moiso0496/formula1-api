from api.controller.race import Result

class Session:
    def __init__(self, session_id, race_id, result_collection) -> None:
        self.session_id = session_id
        self.race_id = race_id
        self.result_collection = result_collection

    def create_driver_result(self, driver_result):
        race_controller = Result(self.race_id, self.result_collection) 
        driver_result["session_id"] = self.session_id
        result = race_controller.manage_race(self.race_id, driver_result)
        return result
        