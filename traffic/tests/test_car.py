import pytest
import car

class TestClass(object):
    def test_constructor(self):
        my_car = car()
        assert my_car
