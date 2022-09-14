from api.controller.race import Result
from api.controller.session import Session
from api.utils.validate_schema import create_validate_schema


class RaceResult:
    def __init__(self, model, result_collection) -> None:
        self.model = model
        self.result_collection = result_collection
    

    def get_all_races_results(self):
        results = Result(self.result_collection)
        return results.get_all_races()
        


    def create_driver_result(self, driver_result):
        # all_good = create_validate_schema(driver_result, self.model, "create")
        all_good = True
        if all_good == True:
            session_controller = Session(driver_result["session_id"], driver_result["race_id"], self.result_collection)    
            result = session_controller.create_driver_result(driver_result)
            return result
        else:
            return all_good

