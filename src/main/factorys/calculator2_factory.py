from src.calculators.calculator_2 import Calculator2
from src.drivers.numpy_handler import NumpyHandler

def calculator2_factory():
    numpyhandler = NumpyHandler()
    calc = Calculator2(numpyhandler)
    return calc