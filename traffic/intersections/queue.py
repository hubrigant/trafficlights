from cars.car import Car
from typing import List


class QueueFullError(TypeError):
    def __init__(self, error_text:str):
        self.__error_text = error_text


class Queue:
    'Defines a queue of cars'
    def __init__(self, queue_id:str, max_queue_depth:int = 10):
        self.__max_queue_depth = max_queue_depth
        self.__queue_id = queue_id
        self.__cars = []
        self.__index = 0
        self.__state = 'waiting'
        self.__next_queue = self


    def add_car(self, car:Car):
        if len(self.__cars) < self.__max_queue_depth:
            self.__cars.append(car)
            return len(self.__cars)
        else:
            # raise error because queue is full
            raise QueueFullError(("Queue '{0}' already full with {1} cars"
                                 ).format(self.__queue_id, len(self.__cars)))


    def fill(self):
        for _ in range(self.__max_queue_depth):
            self.add_car(Car(queue_id = self.__queue_id))
        return len(self)


    def add_cars(self, cars:List[Car]):
        for i in range(len(cars)):
            self.add_car(cars[i])
        return len(self.__cars)


    def empty(self):
        self.__cars = []


    def pop(self, index:int = None):
        if index:
            return self.__cars.pop(index)
        else:
            return self.__cars.pop()

    def get_variables(self):
        return {'max_queue_depth': self.__max_queue_depth,
                'queue_id': self.__queue_id,
                'cars': self.__cars,
                'num_cars': len(self),
                'state': self.__state}


    def __str__(self):
        return ('Queue {0}:\n\tState: {1}\n' \
                '\tMax Depth: {2}\n\tCars: {3}\n\tNum Cars: {4}'
                ).format(self.__queue_id,
                         self.__state,
                         self.__max_queue_depth,
                         self.__cars,
                         str(len(self)))


    def __len__(self):
        return len(self.__cars)


    def __getitem__(self, key: int = 0):
        return self.__cars[key]


    def __iter__(self):
        return self


    def __next__(self):
        try:
            result = self.__cars[self.__index]
        except IndexError:
            raise StopIteration
        self.__index += 1
        return result


    def __contains__(self, item):
        return item in self.__cars


    def is_full(self):
        if len(self) == self.__max_queue_depth:
            return True
        else:
            return False


    def notify(self, can_move: bool):
        if can_move:
            self.__state = 'moving'
        return self.__state, len(self)
