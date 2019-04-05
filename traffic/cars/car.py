import random

class Car:
    'Defines a single car with its queue status and wait time'
    def __init__(self, queue_id:str, latency:int = random.randrange(1,6)):
        self.queue_id = queue_id
        self.latency = latency
        self.time_waiting = 0


    def __str__(self):
        return 'Queue ID: {0}; Latency: {1}'.format(self.queue_id, self.latency)
