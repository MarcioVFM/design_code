from src.drivers.numpy_handler import NumpyHandler
from src.calculators.calculator_3 import Calculator3

def calculator3_factory():
    numpy_habdler = NumpyHandler()
    calc = Calculator3(numpy_habdler)
    return calc