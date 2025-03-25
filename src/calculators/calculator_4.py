from flask import request as FlaskRequequest
from src.errors.http_unprocesssable_entity import HttpUnprocessableEntityError

class Calculator4:
    def calculate(self, request: FlaskRequequest) -> dict: #type:ignore
        body = request.json
        input_data = self.__validate_body(body)
        average = self.__calculate_average(input_data)
        format_response = self.__format_response(average)
        return format_response

    def __validate_body(self, body: dict) -> list[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("body mal formatado")
        
        input_data = body["numbers"]
        return input_data
    
    def __calculate_average(self, input_data) -> float:
        average = sum(input_data) / len(input_data)
        return average
    
    def __format_response(self, average) ->dict:
        return {
            "data": {
                "Calculator": 4,
                "result": round(average, 2)
            }
        }
