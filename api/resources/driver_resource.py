from flask_restful import Resource
from api.controller.driver import Driver
from api.model.driver_shema import driverSchema

from api.controller.driver_db import DriverDataBase

class DriverResource(Resource):
    driver_db = DriverDataBase("mongodb://docker:mongopw@127.0.0.1:55000")
    driver = Driver(driverSchema,driver_db)
    

    def post(self):
        create = self.driver.create_driver({
            "driver_num" : "44",
            "driver_first_name" : "Lewis",
            "driver_last_name" :"Hamilton",
            "driver_birth_date": "",
            "driver_team": "Mercedes Benz"
        })

        if create == "Driver succesfully created":
            return {"msg":"Driver succesfully created"} , 201
        else:
            return {"msg":"It was not able to create the driver"} , 400

        

    