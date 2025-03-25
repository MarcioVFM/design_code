from .calculator_3 import Calculator3
from src.drivers.interface.driver_handler_interface import DriverHandlerInterface 
from pytest import raises

class MockRequest:
    def __init__(self, body: dict) -> None:
        self.json = body

class MockDriverHandlerError:
    def variance(self, numbers: list[float]) -> float:
        return 3
    
class MockDriverHandler:
    def variance(self, numbers: list[float]) -> float:
        return 100000


def test_calculate_with_variance_error():
    mock_request = MockRequest({"numbers": [1, 2, 3, 4, 5]})
    calculator_3 = Calculator3(MockDriverHandlerError())

    with raises(Exception) as excinfo:
        calculator_3.calculate(mock_request)

    assert str(excinfo.value) == 'Falha no processo: variancia menor que o multiplicador'

def test_calculate():
    mock_request = MockRequest({"numbers": [1, 1, 1, 1, 100]})
    calculator_3 = Calculator3(MockDriverHandler())

    response = calculator_3.calculate(mock_request)
    
    assert response == {'data': {'Calculator': 3, 'value': 100000, 'Success': True}}