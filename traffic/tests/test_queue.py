import pytest
import collections
from cars.car import Car
from intersections.queue import Queue, QueueFullError

class TestClass(object):
    def test_constructor(self):
        with pytest.raises(TypeError):
            my_queue = Queue()
        my_queue = Queue(queue_id = "test1", max_queue_depth = 10)
        assert my_queue.name == "test1"


    def test_add_remove(self):
        my_queue = Queue(queue_id = "test2", max_queue_depth = 2)
        my_car = Car(queue_id = "test2")
        assert my_queue.add_car(my_car) == 1
        assert my_queue.add_car(my_car) == 2
        with pytest.raises(QueueFullError):
            my_queue.add_car(my_car)
        assert my_queue.remove_car() == 1
        assert my_queue.pop() == my_car
        assert len(my_queue) == 0


    def test_iterator(self, build_queue):
        my_queue = build_queue
        my_car = Car(queue_id = my_queue.name)
        for _ in range(my_queue.max_queue_depth):
            my_queue.add_car(my_car)
        my_queue_list = my_queue.get_list()
        assert len(my_queue_list) == 10
        assert my_queue[1] == my_car
        assert isinstance(my_queue, collections.Iterable)
        assert my_car in my_queue


    def test_contains(self, fill_queue):
        my_queue = fill_queue
        my_car = my_queue[0]
        assert my_car in my_queue
