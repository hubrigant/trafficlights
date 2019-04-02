import pytest
from car import car


class TestCar():
    def test__init__(self):
        my_car = car.car()
        assert my_car.time_waiting == 0


    def test_update_queue_id(self):
        my_car = car.car()
        assert car1.queue_id == 'left side a'
        car1.queue_id = 'left funnel'
        assert car1.queue_id == 'left funnel'
