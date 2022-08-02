from flask import jsonify, request

from flask_restful import Resource
from api.controller.driver import Driver
from api.model.driver_shema import driverSchema
from api.controller.driver_db import DriverDataBase
from api.model.data_type.data_type import data_types

class DriverResource(Resource):
    driver_db = DriverDataBase("mongodb://docker:mongopw@127.0.0.1:55000")
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
                    return {"msg" : "Driver not found"}, 404
                elif delete.deleted_count == 1:
                    return {"msg":"Driver successfully deleted"} , 201
            else:
                return {"msg":"It was not possible to delete the driver", "error": delete} , 400
        else:
            return {"msg": "No valid JSON Data sent on the request"} , 400
    
    def patch(self):
        data = request.get_json()
        driver_num = request.args.get(("driver_num"))
        if  driver_num and data != {}:
            driver_query = {"driver_num": int(driver_num)}
            update = self.driver.update_driver(driver_query, data)
            if type(update) != data_types["String"]:
                if update.matched_count == 0:
                    return {"msg" : "Driver not found"} , 404
                elif update.modified_count == 0:
                    return {"msg" : "No modifications were done"}, 412
                elif update.modified_count == 1:
                    return {"msg":"Driver successfully updated"} , 204
            else:
                return {"msg":"It was not possible to update the driver", "error": update} , 400
        elif data == {}:
            return {"msg": "No valid JSON Data sent on the request"} , 400
        elif not driver_query:
            return {"msg" : "No query string driver_num found on the request"} , 400
            



        

    