from flask import request as FlaskRequest
from src.drivers.interface.driver_handler_interface import DriverHandlerInterface
from src.errors.http_unprocesssable_entity import HttpUnprocessableEntityError

class Calculator2:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> dict:#type:ignore
        body = request.json
        input_data = self.__validate_body(body)
        calculated_number = self.__process_data(input_data)
        format_response = self.__format_response(calculated_number)
        return format_response 

    def __validate_body(self, body: dict) -> list[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("body mal formatado")
        
        input_data = body['numbers']
        return input_data
    
    def __process_data(self, input_data: list[float]) -> float:
        first_process_result = [(num * 11) ** 0.95 for num in input_data]
        result = self.__driver_handler.standard_derivation(first_process_result)
        return 1/result
    
    def __format_response(self, calc_result: float) -> dict:
        return {
            "data": {
                "Calculator": 2,
                "result": float(round(calc_result,2))
            }
        }

