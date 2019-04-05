import pytest
from cars.car import Car
from intersections.queue import Queue

class TestClass(object):
    def test_constructor(self):
        with pytest.raises(TypeError):
            my_queue = Queue()
        my_queue = Queue(queue_name = "test1", max_queue_depth = 10)
        assert my_queue.name == "test1"


    def test_add_remove(self):
        my_queue = Queue(queue_name = "test2", max_queue_depth = 2)
        my_car = Car(queue_id = "test2")
        assert my_queue.add_car(my_car) == 1
        assert my_queue.add_car(my_car) == 2
        assert my_queue.remove_car() == 1
        #my_car = Car(queue_id = 'test queue')
        #assert my_car.queue_id == 'test queue'
        #assert my_car.latency > 0
        #my_car2 = Car(queue_id = 'test queue', latency = 1)
        #assert my_car2.latency == 1
