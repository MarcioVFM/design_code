from flask import request as FlaskRequest
from src.errors.http_unprocesssable_entity import HttpUnprocessableEntityError

class Calculator1:
    def calculate(self, request: FlaskRequest) -> dict: #type:ignore
        body = request.json
        input_data = self.__validate_body(body)
        splited_number = input_data / 3

        first_process_result = self.__first_process(splited_number)
        second_process_result = self.__second_process(splited_number)
        thirth_part = splited_number
        calc_result = first_process_result + second_process_result + thirth_part

        response = self.__format_response(calc_result)
        return response

    def __validate_body(self, body: dict) -> float:
        if "number" not in body:
            raise HttpUnprocessableEntityError("body mal formatado")
        
        input_data = body["number"]
        return input_data
        
    def __first_process(self, num1: float) -> float:
        first_part = (num1 / 4) + 7
        second_part = (first_part ** 2) * 0.257
        return second_part
    
    def __second_process(self, num2: float) -> float:
        first_part = (num2 ** 2.212)
        second_part = (first_part / 5) + 1
        return second_part
    
    def __format_response(self, calc_result: float) -> dict:
        return {
            "data": {
                "Calculator": 1,
                "result": round(calc_result, 2)
            }
        }