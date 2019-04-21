import pytest
from cars.car import Car


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
        assert my_car.set_value(variable = 'last_distance_moved',
                                value = '66',
                                type='int')

    def test_str_output(self):
        my_car = Car(queue_id = 'str test')
        assert str(my_car) == 'Queue ID: str test; State: waiting, ' \
                              'Latency: 0, Moved: 0, Waiting: 0, Last Moved: 0'

    def test_notify(self):
        my_car = None
        my_car = Car(queue_id = 'notify method test')
        assert my_car.get_variables()['time_waiting'] == 0
        assert my_car.notify(can_move = True) == ('reacting', 0, 0)
        assert my_car.get_variables()['latency'] >= 1
        assert my_car.get_variables()['distance_moved'] == 0
        my_car.set_value(variable = 'latency', value = '1', type = 'int')
        assert my_car.notify(can_move = True) == ('reacting', 0, 0)
        assert my_car.get_variables()['time_waiting'] == 2
        assert my_car.notify(can_move = True) == ('moving', 0, 1)
        assert my_car.notify(can_move = True) == ('moving', 1, 2)
        assert my_car.notify(can_move = False) == ('waiting', 1, 2)
        assert my_car.get_variables()['last_distance_moved'] == 1
