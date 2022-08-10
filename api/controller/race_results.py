from api.controller.session import Session
from api.utils.validate_schema import create_validate_schema


class RaceResult:
    def __init__(self, model, result_collection) -> None:
        self.model = model
        self.result_collection = result_collection
    

    def create_driver_result(self, driver_result, session_id, race_id):
        all_good = create_validate_schema(driver_result, self.model, "create")
        if all_good == True:
            session_controller = Session(session_id, race_id, self.result_collection)    
            result = session_controller.create_driver_result(driver_result)
            return result
        else:
            return all_good

