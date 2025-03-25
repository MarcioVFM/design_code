from .calculator_1 import Calculator1
from pytest import raises

class MockRequest:
    def __init__(self, body: dict) -> None:
        self.json = body

def test_calculate():
    mock_request = MockRequest(body={"number": 1})
    calculator_1 = Calculator1()

    response = calculator_1.calculate(mock_request)

    assert "data" in response
    assert "Calculator" in response["data"]
    assert "result" in response["data"]


    assert response["data"]["result"] == 14.25
    assert response['data']['Calculator'] == 1

def test_calculate_with_body_error():
    mock_request = MockRequest(body={"something": 0})
    calculator_1 = Calculator1()

    with raises(Exception) as exinfo:  
        calculator_1.calculate(mock_request)

    assert str(exinfo.value) == "body mal formatado"
    