import pytest
from cars.car import Car
import sys

class TestClass(object):
    def test_constructor(self):
        with pytest.raises(TypeError):
            my_car = Car()
        my_car = Car(queue_id = 'test queue')
        assert my_car.get_variables()['queue_id'] == 'test queue'
        assert my_car.get_variables()['state'] == 'waiting'
        assert my_car.get_variables()['distance_moved'] == 0


    def test_private_variables(self):
        my_car = Car(queue_id = 'private test')
        for variable in ['my_car.latency',
                         'my_car.state',
                         'my_car.queue_id',
                         'my_car.distance_moved']:
            with pytest.raises(AttributeError):
                eval(variable)


    # def test_get_variables(self):
    #     my_car = Car(queue_id = 'get_variables test')
    #     assert my_car.get_variables()['latency'] == 0


    def test_set_value(self):
        my_car = Car(queue_id = 'set_value test')
        assert my_car.set_value(variable = 'latency',
                                value='1',
                                type='int') == 1
        assert my_car.set_value(variable = 'queue_id',
                                value='set test',
                                type='str') == 'set test'
        assert my_car.set_value(variable = 'time_waiting',
                                value='9',
                                type='int') == 9
        assert my_car.set_value(variable = 'state',
                                value='moving',
                                type='str') == 'moving'
        assert my_car.set_value(variable = 'distance_moved',
                                value='99',
                                type='int') == 99

    def test_str_output(self):
        my_car = Car(queue_id = 'str method test')
        assert str(my_car) == 'Queue ID: str method test; Latency: 0, Moved: 0'


    def test_notify(self):
        my_car = None
        my_car = Car(queue_id = 'notify method test')
        assert my_car.get_variables()['time_waiting'] == 0
        print("Test> b4 first notify()")
        assert my_car.notify(can_move = True) == ('reacting', 0) # wait->react
        assert my_car.get_variables()['latency'] >= 1
        assert my_car.get_variables()['distance_moved'] == 0
        my_car.set_value(variable = 'latency', value = '1', type = 'int')
        print("Test> b4 2nd notify()")
        assert my_car.notify(can_move = True) == ('reacting', 0) #
        assert my_car.get_variables()['time_waiting'] == 2
        print("Test> b4 3rd notify()")
        assert my_car.notify(can_move = True) == ('moving', 1)
        print("Test> b4 4th notify()")
        assert my_car.notify(can_move = True) == ('moving', 2)
