from api.utils.validate_schema import create_validate_schema, validate_schema_or_query

class Driver:
    def __init__(self, model, driver_collection) -> None:
        self.model = model
        self.driver_collection = driver_collection  
    
    def get_driver(self, driver_query):
        all_good = validate_schema_or_query(driver_query, self.model)
        if all_good == True:
            result = self.driver_collection.get_document(driver_query)
            return result
        else:
            return all_good
        
    
    def create_driver(self, driver_dict):
        all_good = create_validate_schema(driver_dict, self.model)
        if all_good == True:
            result = self.driver_collection.create_document(driver_dict)
            return result
        else:
            return all_good

    def update_driver(self, _update_query, _update_driver_dict):
        all_good = validate_schema_or_query(_update_driver_dict, self.model)
        if all_good == True:
            result = self.driver_collection.update_document(_update_query, _update_driver_dict)
            return result
        else:
            return all_good

    def delete_driver(self, _delete_query):
        all_good = validate_schema_or_query(_delete_query, self.model)
        if all_good == True:
            result = self.driver_collection.delete_document(_delete_query)
            return result
        else:
            return all_good