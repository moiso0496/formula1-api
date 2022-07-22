from api.utils.validate_schema import validate_schema

class Driver:
    def __init__(self, model, driver_collection) -> None:
        self.model = model
        self.driver_collection = driver_collection  
    
    def get_driver(self, driver_query):
        self.driver_collection.get_document(driver_query)
        pass
    
    def create_driver(self, driver_dict):
        all_good = validate_schema(driver_dict, self.model)
        if all_good == True:
            self.driver_collection.create_document(driver_dict)
            return "Driver succesfully created"
        else:
            return all_good

    def update_driver(self):
        pass

    def delete_driver(self):
        pass