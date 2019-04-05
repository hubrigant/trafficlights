import pytest
from cars.car import Car

class TestClass(object):
    def test_constructor(self):
        with pytest.raises(TypeError):
            my_car = Car()
        my_car = Car(queue_id = 'test queue')
        assert my_car.queue_id == 'test queue'
        assert my_car.latency > 0
        my_car2 = Car(queue_id = 'test queue', latency = 1)
        assert my_car2.latency == 1


    def test_str_output(self):
        my_car = Car(queue_id = 'str method test', latency = 3)
        assert str(my_car) == 'Queue ID: str method test; Latency: 3'
