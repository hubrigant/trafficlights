import random

class Car:
    'Defines a single car with its queue status and wait time'
    def __init__(self, queue_id:str):
        print("I was just born")
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
        return ('Queue ID: {0}; Latency: {1}, Moved: {2}'
               ).format(self.__queue_id,
                        self.__latency,
                        self.__distance_moved
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
                self.__distance_moved = 0
                print(("I was waiting, now I'm reacting ({0}), I've moved {1}"
                      ).format(self.__latency, self.__distance_moved))
            elif self.__state == 'reacting':
                if self.__latency > 0:
                    print("I am still reacting, latency is {0}".format(self.__latency))
                    self.__latency -= 1
                else:
                    self.__state = 'moving'
                    self.__distance_moved += 1
                    print(("I am no longer reacting, I've moved {0}"
                          ).format(self.__distance_moved))
            elif self.__state == 'moving':
                self.__distance_moved += 1
                print("I am already moving, I've moved  {0}".format(self.__distance_moved))
        return self.__state, self.__distance_moved
