def validate_schema(_dic, _model):
    for field in _model:
        if _model[field]["required"]:
                if field not in _dic:
                    return f"Not able to create driver, {field} not found on the dictionary"
    return True