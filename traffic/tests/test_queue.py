import pytest
import collections
from cars.car import Car
from intersections.queue import Queue, QueueFullError
from cars.fleet import Fleet

class TestClass(object):
    def test_constructor(self):
        with pytest.raises(TypeError):
            my_queue = Queue()
        my_queue = Queue(queue_id = "test1", max_queue_depth = 10)
        assert my_queue.get_variables()['queue_id'] == "test1"


    def test_set_value(self, build_queue):
        my_queue = build_queue
        my_queue.set_value(variable = 'max_queue_depth',
                           value = '99',
                           type = 'int'
                          )
        assert my_queue.get_variables()['max_queue_depth'] == 99


    def test_get_variables(self):
        my_queue = Queue(queue_id = "get variables", max_queue_depth = 2)
        assert my_queue.get_variables() == {'max_queue_depth': 2,
                                            'queue_id': 'get variables',
                                            'cars': [],
                                            'num_cars': 0,
                                            'state': 'waiting'
                                           }


    def test_add_remove(self):
        my_queue = Queue(queue_id = "test2", max_queue_depth = 4)
        my_car = Car(queue_id = "test2")
        assert my_queue.add_car(my_car) == 1
        assert my_queue.add_car(my_car) == 2
        assert my_queue.add_car(my_car) == 3
        assert my_queue.add_car(my_car) == 4
        with pytest.raises(QueueFullError):
            my_queue.add_car(my_car)
        assert my_queue.pop() == my_car
        assert my_queue.pop(1) == my_car
        assert len(my_queue) == 2


    def test_add_remove_multiple(self):
        my_queue = Queue(queue_id = "test3", max_queue_depth = 5)
        my_fleet = Fleet(my_queue.get_variables()['queue_id'],
                         quantity=my_queue.get_variables()['max_queue_depth'])
        my_queue.add_cars(my_fleet.get_list())
        assert len(my_queue) == my_queue.get_variables()['max_queue_depth']
        my_queue.empty()
        assert len(my_queue) == 0
        my_fleet = Fleet(my_queue.get_variables()['queue_id'], quantity=5)
        my_queue.add_cars(my_fleet.get_list())
        assert len(my_queue) == 5


    def test_fill_queue(self):
        my_queue = Queue(queue_id = "test fill queue", max_queue_depth = 10)
        my_queue.fill()
        assert len(my_queue) == my_queue.get_variables()['max_queue_depth']


    def test_iterator(self, build_queue):
        my_queue = build_queue
        my_car = Car(queue_id = my_queue.get_variables()['queue_id'])
        for _ in range(my_queue.get_variables()['max_queue_depth']):
            my_queue.add_car(my_car)
        my_queue_list = my_queue.get_variables()['cars']
        assert len(my_queue_list) == 10
        assert my_queue[1] == my_car
        assert isinstance(my_queue, collections.Iterable)
        car_counter = 0
        for _ in my_queue:
            car_counter += 1
        assert car_counter == len(my_queue)


    def test_contains(self, fill_queue):
        my_queue = Queue(queue_id = "test3", max_queue_depth = 7)
        for _ in range(my_queue.get_variables()['max_queue_depth']):
            my_queue.add_car(Car(queue_id = my_queue.get_variables()['queue_id']))
        my_car = my_queue[0]
        assert my_car in my_queue


    def test_str_output(self, build_queue):
        my_queue = build_queue
        my_queue.add_car(Car(queue_id = my_queue.get_variables()['queue_id']))
        queue_vars = my_queue.get_variables()
        assert str(my_queue) == ('Queue {0}:\n\tState: {1}\n' \
                                '\tMax Depth: {2}\n\tCars: {3}\n'\
                                '\tNum Cars: {4}'
                                ).format(queue_vars['queue_id'],
                                         queue_vars['state'],
                                         queue_vars['max_queue_depth'],
                                         queue_vars['cars'],
                                         len(my_queue))


    def test_is_full(self, build_queue):
        my_queue = build_queue
        print(my_queue)
        my_queue.fill()
        assert my_queue.is_full() == True


    def test_notify(self, fill_queue):
        my_queue = fill_queue
        my_queue.get_variables()['state'] == 'waiting'
        assert my_queue.notify(can_move = True) == ('moving', len(my_queue))
