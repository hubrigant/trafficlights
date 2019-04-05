import pytest
from cars.fleet import Fleet
from cars.car import Car
from intersections.queue import Queue

@pytest.fixture
def build_fleet():
    return Fleet(queue_id='test')


@pytest.fixture
def build_queue():
    return Queue(queue_id='fixture queue')


@pytest.fixture
def fill_queue():
    my_queue = Queue(queue_id = 'fixture full queue', max_queue_depth = 10)
    for _ in range(my_queue.max_queue_depth):
        my_queue.add_car(Car(queue_id = my_queue.name))
    return my_queue
