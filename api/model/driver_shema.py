driverSchema = {
    "driver_num" : {
    "type": "Number",
    "required": True
    },
    "driver_first_name" : {
        "type": "String",
        "required": True
    },
    "driver_last_name" :{
        "type": "String",
        "required": True
    },
    # TODO change driver_birth to requiered True
    "driver_birth_date":{
        "type": "Date",
        "required": False
    },
    "driver_team":{
        "type": "String",
        "required": True
    }
}