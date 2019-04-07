import random

class Car:
    'Defines a single car with its queue status and wait time'
    def __init__(self, queue_id:str):
        self.__queue_id = queue_id
        self.__latency = 0
        self.__time_waiting = 0
        self.__state = 'waiting'
        self.__distance_moved = 0


    def set_value(self, variable: str, value: str, type: str):
        if type == 'int':
            my_value = int(value)
        else:
            my_value = value
        if variable == 'queue_id':
            self.__queue_id = my_value
            return self.__queue_id
        if variable == 'latency':
            self.__latency = my_value
            return self.__latency
        if variable == 'time_waiting':
            self.__time_waiting = my_value
            return self.__time_waiting
        if variable == 'state':
            self.__state = my_value
            return self.__state
        if variable == 'distance_moved':
            self.__distance_moved = my_value
            return self.__distance_moved


    def __str__(self):
        return ('Queue ID: {0}; State: {1}, Latency: {2}, Moved: {3}, Waiting: {4}'
               ).format(self.__queue_id,
                        self.__state,
                        self.__latency,
                        self.__distance_moved,
                        self.__time_waiting
                        )


    def get_variables(self):
        return {'latency': self.__latency,
                'state': self.__state,
                'queue_id': self.__queue_id,
                'distance_moved': self.__distance_moved,
                'time_waiting': self.__time_waiting
               }


    def notify(self, can_move: str):
        self.__time_waiting += 1
        if can_move:
            if self.__state == 'waiting':
                self.__state = 'reacting'
                self.__latency = random.randrange(2,7)
            elif self.__state == 'reacting':
                if self.__latency > 0:
                    self.__latency -= 1
                else:
                    self.__state = 'moving'
                    self.__distance_moved += 1
            elif self.__state == 'moving':
                self.__distance_moved += 1
        else:
            self.__state = 'waiting'
        return self.__state, self.__distance_moved
