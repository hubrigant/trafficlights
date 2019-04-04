import pytest
from cars.fleet import Fleet
import collections

class TestClass(object):
    def test_constructor(self, build_fleet):
        with pytest.raises(TypeError):
            my_fleet = Fleet()
        my_fleet = Fleet(queue_id='test')
        assert my_fleet
        assert my_fleet.quantity == 10
    

    def test_iterator(self):
        my_fleet = Fleet(queue_id='test')
        my_list_of_cars = my_fleet.get_list()
        assert isinstance(my_fleet, collections.Iterable)
        assert my_list_of_cars[0] == my_fleet[0]
        assert my_list_of_cars[0] in my_fleet


    def test_get_methods(self):
        my_fleet = Fleet(queue_id='test')
        my_list_of_cars = my_fleet.get_list()
        assert type(my_list_of_cars) == list


    def test_contains(self):
        my_fleet = Fleet(queue_id='test')
        my_list_of_cars = my_fleet.get_list()
        assert my_list_of_cars[0] in my_fleet

