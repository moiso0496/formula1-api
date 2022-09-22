from api.utils.validate_schema import create_validate_schema
from api.model.data_type.data_type import data_types


class Driver:
    def __init__(self, model, driver_collection) -> None:
        self.model = model
        self.driver_collection = driver_collection  
    
    def get_drivers(self, driver_query=None, filter_query={}):
        result = None
        if not driver_query:
            result = self.driver_collection.get_all_documents(filter_query)
        else:
            result = self.driver_collection.get_one_document_with_filter_values(driver_query, filter_query)
        if not result:
            return f'No drivers found'
        return result if type(result) == data_types["Dictionary"] else list(result)

        
    
    def create_driver(self, driver_dict):
        all_good = create_validate_schema(driver_dict, self.model, "create")
        if all_good == True:
            result = self.driver_collection.create_document(driver_dict)
            return result.acknowledged
        else:
            return all_good

    def update_driver(self, _update_query, _update_driver_dict):
        all_good = create_validate_schema(_update_driver_dict, self.model, "update")
        if all_good == True:
            result = self.driver_collection.update_document(_update_query, _update_driver_dict)
            return result
        else:
            return all_good

    def delete_driver(self, _delete_query):
        all_good = create_validate_schema(_delete_query, self.model, "delete")
        if all_good == True:
            result = self.driver_collection.delete_document(_delete_query)
            return result
        else:
            return all_good