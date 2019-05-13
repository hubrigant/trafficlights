import pytest
# import collections
# from cars.car import Car
from intersections.queue import Queue
from intersections.stoplight import Stoplight


class TestClass(object):
    def test_constructor(self):
        with pytest.raises(TypeError):
            my_stoplight = Stoplight()
        # in_queue = Queue(queue_id='in_queue')
        # out_queue = Queue(queue_id='out_queue')
        my_two_queue_light = Stoplight(in_queues=[Queue(queue_id='in_queue')],
                                       out_queues=[Queue(queue_id='out_queue')])
        assert my_two_queue_light.num_inputs() == 1
        # my_queue = Queue(queue_id="test1", max_queue_depth=10)
        # assert my_queue.get_variables()['queue_id'] == "test1"
