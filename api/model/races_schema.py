result_schema = {
    "result_id":{
    "type": "String",
    "required": True
    },
    "driver_num":{
    "type": "Number",
    "required": True
    },
    "driver_position": {
    "type": "Number",
    "required": True
    },
    "driver_best_time":{
    "type": "Number",
    "required": True
    }
}

session_schema = {
    "session_id":{
    "type": "String",
    "required": True
    },
    "session_results" : result_schema
}

races_schema={
    "race_id" : {
    "type": "String",
    "required": True
    },
    "practice_one_results" : session_schema,
    "practice_two_results" : session_schema,
    "practice_three_results": session_schema,
    "qualifying_results": {"Q1": session_schema,
                        "Q2": session_schema,
                        "Q3": session_schema},
    "race_results" : session_schema
}