def create_validate_schema(_dic, _model):
    valid_schema = validate_schema_or_query(_dic,_model)
    if valid_schema:
        for field in _model:
            if _model[field]["required"]:
                    if field not in _dic:
                        return f"Not able to create driver, {field} not found on the dictionary"
    else:
        return valid_schema
        
    return True

def validate_schema_or_query(_dic, _model):
    for field in _dic:
        if field not in _model:
            return f"Wrong schema presented,  {field} not in schema"
    return True