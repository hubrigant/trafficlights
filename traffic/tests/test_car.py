import pytest
from cars.car import Car

class TestClass(object):
    def test_constructor(self):
        with pytest.raises(TypeError):
            my_car = Car()
        assert Car(queue_id = 'test queue')
