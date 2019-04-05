from cars.car import Car


class Fleet:
    'Bulk-builds multiple cars'
    def __init__(self, queue_id:str, quantity:int = 10):
        self.quantity = quantity
        self.queue_id = queue_id
        self.index = 0
        self.cars = []
        for _ in range(self.quantity):
            self.cars.append(Car(queue_id = self.queue_id))

    def get_list(self):
        return self.cars


    def __iter__(self):
       return self


    def __next__(self):
        try:
            result = self.cars[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return result


    def __getitem__(self, key:int):
        return self.cars[key]


    def __len__(self):
        return len(self.cars)


    def __contains__(self, item):
        return item in self.cars
