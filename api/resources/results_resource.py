import json
from flask import jsonify, request

from flask_restful import Resource
from api.controller.results_db import ResultsDataBase
from api.controller.race_results import RaceResult
from api.model.races_schema import result_schema
from api.model.data_type.data_type import data_types

RESULT_DB = ResultsDataBase("mongodb://api_user:apipassword@127.0.0.1:27017/?authSource=fsd-formula1&readPreference=primary&ssl=false")
class ResultsResource(Resource):
    results = RaceResult(result_schema, RESULT_DB)

    def get(self):
        query = request.args
        filter = json.loads(query["filter"]) if "filter" in query else {}
        races = None
        if "race_id" in query:
            race_num = {"race_id": query["race_id"]}
            races = self.results.get_races_results(race_num, filter)
        else:
            races = self.results.get_races_results(filter_query=filter)
        if type(races) == data_types["List"]:
            return jsonify(races)
        else:
            if not races:
                return {"msg" : "Driver not found"}
            else:
                return {"msg" : races}
    
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


