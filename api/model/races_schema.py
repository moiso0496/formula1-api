result_schema = {
    "driver_num":{},
    "driver_position": {},
    "driver_best_time":{}
}

session_schema = {
    "session_id":{},
    "session_results" : [result_schema]
}

races_schema={
    "race_id" : {},
    "practice_one_results" : session_schema,
    "practice_two_results" : session_schema,
    "practice_three_results": session_schema,
    "qualifying_results": session_schema,
    "race_results" : session_schema
}