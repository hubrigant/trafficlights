import pytest
from car import car


class TestCar():
    def test_constructor(self):
        my_car = car()
        assert my_car.time_waiting == 0

