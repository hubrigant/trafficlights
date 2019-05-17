'''
Fixtures for unit tests of intersections package
'''

import pytest
from cars.car import Car
from intersections.queue import Queue
from intersections.stoplight import Stoplight


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


@pytest.fixture
def two_queue_intersection():
    '''
    Builes a simple intersection with a Stoplight controling access from
    one input Queue to one output Queue
    '''
    input_queue = Queue(queue_id="input queue", max_queue_depth=1)
    ouptut_queue = Queue(queue_id="output queue", max_queue_depth=1)
    my_car = Car(queue_id="input queue")
    my_car.set_value(variable="state", value="moving", type="str")
    my_car.set_value(variable="distance_moved", value="2", type="int")
    my_car.set_value(variable="last_distance_moved", value="1", type="int")
    input_queue.add_car(my_car)
    my_stoplight = Stoplight(in_queues=[input_queue],
                             out_queues=[ouptut_queue],
                             duration=15)
    return my_stoplight
