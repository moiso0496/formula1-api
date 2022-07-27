from api.model.data_type.data_type import data_types

def create_validate_schema(_dic, _model, _action):
    read = "get"
    create = "create"
    update = "update"
    delete = "delete"
    
    if _action == create:        
            required_field = validate_required_fields( _model,_dic)
            if required_field != True:
                return required_field
                
    for field in _dic:
        if _action in [read,create,update,delete]:
            valid_structure = validate_correct_structure(field, _model)
            if valid_structure != True:
                return valid_structure
        
        if _action in [read,create,update,delete]:
            data_type = validate_data_type(_model[field]["type"], _dic[field], field)
            if data_type != True:
                return data_type
    return True

def validate_data_type(_data_type, field,_field):
    if data_types[_data_type] == type(field):
        return True
    else:
        return f"Wrong data type for field {_field}, expected a {data_types[_data_type]} received a {type(field)}"

def validate_correct_structure(field, _model):
    if field not in _model:
            return f"Wrong field presented,  {field} not in schema"
    return True

def validate_required_fields(_model,_dic):
    for field in _model:
        if _model[field]["required"]:
            if field not in _dic:
                return f"Not able to create driver, {field} not found on the JSON payload"
    return True