def create_response(code, message=None, data=None):
    return {
        "code": code,
        "message": message,
        "data": data
    }
