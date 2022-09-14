from flask import jsonify, request

from flask_restful import Resource
from api.controller.results_db import ResultsDataBase
from api.controller.race_results import RaceResult
from api.model.races_schema import result_schema


class ResultsResource(Resource):
    result_db = ResultsDataBase("mongodb://api_user:apipassword@127.0.0.1:27017/?authSource=fsd-formula1&readPreference=primary&ssl=false")
    results = RaceResult(result_schema, result_db)


    def get(self):
        races = self.results.get_all_races_results()
        return races , 200
    
    def post(self):
        data = request.get_json()
        if data != {}:
            create = self.results.create_driver_result(data)
            if create == True:
                return {"msg":"Result successfully added"} , 201
            else:
                return {"msg":"It was not possible to add the result", "error": create} , 400
        else:
            return {"msg": "No valid JSON Data sent on the request"} , 400
