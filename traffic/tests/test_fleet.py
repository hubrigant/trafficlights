import pytest
from cars.fleet import Fleet

class TestClass(object):
    def test_constructor(self):
        with pytest.raises(TypeError):
            my_fleet = Fleet()
        my_fleet = Fleet(queue_id = 'test queue')
        assert my_fleet
        assert my_fleet.quantity == 10
        my_list_of_cars = my_fleet.get_list()
        #assert my_car.queue_id == 'test queue'
        #assert my_car.latency > 0
        #my_car2 = Car(queue_id = 'test queue', latency = 1)
        #assert my_car2.latency == 1
