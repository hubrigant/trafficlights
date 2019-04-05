from cars.car import Car
from typing import List


class QueueFullError(TypeError):
    def __init__(error_text:str):
        self.error_text = error_text


class Queue:
    'Defines a queue of cars'
    def __init__(self, queue_name:str, max_queue_depth:int):
        self.max_queue_depth = max_queue_depth
        self.name = queue_name
        self.cars = []


    def add_car(self, car:Car):
        if len(self.cars) < self.max_queue_depth:
            self.cars.append(car)
            return len(self.cars)
        else:
            # raise error because queue is full
            raise QueueFullError("Queue {0} already full with {1} cars".format(self.name, len(self.cars)))


    def remove_car(self):
        self.pop_car()
        return len(self.cars)


    def pop_car(self, index:int = -1):
        if index == -1:
            return self.cars.pop()
        else:
            return self.cars.pop(index)

