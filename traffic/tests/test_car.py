import pytest
from cars import Car

class TestClass(object):
    def test_constructor(self):
        my_car = Car()
        assert my_car
