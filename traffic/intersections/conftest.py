'''
Fixtures for unit tests of intersections package
'''


import pytest
from intersections.queue import Queue


@pytest.fixture
def build_queue():
    '''Builds an empty Queue'''
    return Queue(queue_id='fixture queue')


@pytest.fixture
def full_queue():
    '''Builds a Queue that's filled with Cars'''
    my_queue = Queue(queue_id='fixture full queue', max_queue_depth=10)
    my_queue.fill()
    return my_queue
