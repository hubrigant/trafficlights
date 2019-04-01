class queue:
    'Defines a queue of cars'
    def __init__(self, queue_name:str, max_queue_depth:int):
        self.max_queue_depth = max_queue_depth
        self.name = queue_name


    def add_car(self, car:Car):
        if len(self.cars) < self.max_queue_depth:
            self.cars.append(car)
            return cars.index(car)
        else:
            # raise error because queue is full


    def remove_car(self):
        return self.cars.pop(0)

