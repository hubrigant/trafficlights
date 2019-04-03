from cars.car import Car


class Fleet:
    'Bulk-builds multiple cars'
    def __init__(self, queue_id:str, quantity:int = 10):
        self.quantity = quantity
        self.queue_id = queue_id
        self.cars = []
        for i in range(self.quantity):
            self.cars.append(Car(queue_id = self.queue_id))

    def get_list(self):
        return self.cars
