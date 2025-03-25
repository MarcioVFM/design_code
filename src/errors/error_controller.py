from .http_bad_request import HttpBadRequestError
from .http_unprocesssable_entity import HttpUnprocessableEntityError

def handler_errors(error: Exception) -> dict:
    if isinstance(error, (HttpUnprocessableEntityError, HttpBadRequestError)):
        return {
            "status_code": error.status_code,
            "body": {
                "errors":[{
                    "title": error.name,
                    "detail": error.message
                }]

            }
        }
    
    return {
        "statur_code": 500,
        "body": {
            "errors": [{
                "title": "Server Error",
                "detail": str(error)
            }]

        }
    }