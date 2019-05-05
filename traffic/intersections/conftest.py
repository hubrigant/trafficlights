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
def full_queue():
    my_queue = Queue(queue_id='fixture full queue', max_queue_depth=10)
    my_queue.fill()
    return my_queue
