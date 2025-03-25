from .calculator_4 import Calculator4

class MockRequest:
    def __init__(self, body: dict) -> None:
        self.json = body

def test_calculate_intagration():
    mock_request = MockRequest({"numbers": [1, 2, 3, 4]})
    calculator_4 = Calculator4()
    formated_response = calculator_4.calculate(mock_request)

    assert isinstance(formated_response, dict)
    assert formated_response == {'data': {'Calculator': 4, 'result': 2.5}}
