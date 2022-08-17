from flask import jsonify, request

from flask_restful import Resource
from api.controller.driver import Driver
from api.model.driver_shema import driverSchema
from api.controller.driver_db import DriverDataBase
from api.model.data_type.data_type import data_types

class DriverResource(Resource):
    driver_db = DriverDataBase("mongodb://api_user:apipassword@mongo:27017/?authSource=fsd-formula1&readPreference=primary&ssl=false")
    driver = Driver(driverSchema,driver_db)
    

    def post(self):
        data = request.get_json()
        if data != {}:
            create = self.driver.create_driver(data)
            if create == True:
                return {"msg":"Driver successfully created"} , 201
            else:
                return {"msg":"It was not possible to create the driver", "error": create} , 400
        else:
            return {"msg": "No valid JSON Data sent on the request"} , 400
    
    def get(self):
        data = request.get_json()
        if data !={}:
            get_driver = self.driver.get_driver(data)
            if type(get_driver) == data_types["Dictionary"]:
                return jsonify(get_driver)
            else:
                if not get_driver:
                    return {"msg" : "Driver not found"}
                else:
                    return {"msg" : get_driver}
        else:
            return {"msg": "No valid JSON Data sent on the request"} , 400
    
    def delete(self):
        data= request.get_json()
        if data != {}:
            delete = self.driver.delete_driver(data)
            if type(delete) != data_types["String"]:
                if delete.deleted_count == 0:
                    return {"msg" : "Driver not found"}
                elif delete.deleted_count == 1:
                    return {"msg":"Driver successfully deleted"} , 201
            else:
                return {"msg":"It was not possible to delete the driver", "error": delete} , 400
        else:
            return {"msg": "No valid JSON Data sent on the request"} , 400
            



        

    