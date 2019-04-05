from cars.car import Car
from typing import List


class QueueFullError(TypeError):
    def __init__(self, error_text:str):
        self.error_text = error_text


class Queue:
    'Defines a queue of cars'
    def __init__(self, queue_id:str, max_queue_depth:int = 10):
        self.max_queue_depth = max_queue_depth
        self.name = queue_id
        self.cars = []
        self.index = 0


    def add_car(self, car:Car):
        if len(self.cars) < self.max_queue_depth:
            self.cars.append(car)
            return len(self.cars)
        else:
            # raise error because queue is full
            raise QueueFullError("Queue '{0}' already full with {1} cars".format(self.name, len(self.cars)))
            # raise QueueFullError("Queue already full")


    def add_cars(self, cars:List[Car]):
        for i in range(len(cars)):
            self.add_car(cars[i])
        return len(self.cars)

    def remove_car(self):
        self.pop()
        return len(self.cars)


    def empty(self):
        self.cars = []


    def pop(self, index:int = -1):
        if index == -1:
            return self.cars.pop()
        else:
            return self.cars.pop(index)


    def get_list(self):
        return self.cars


    def __len__(self):
        return len(self.cars)


    def __getitem__(self, key: int = 0):
        return self.cars[key]


    def __iter__(self):
        return self


    def __next__(self):
        try:
            result = self.cars[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return result


    def __contains__(self, item):
        return item in self.cars
