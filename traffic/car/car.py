class car:
    'Defines a single car with its queue status and wait time'
    def __init__(self, latency:int = random.randrange(1,6), queue_id:str):
        self.queue_id = queue_id
        self.latency = latency
        self.time_waiting = 0


    def change_queues(self, queue_id:str):
        self.queue_id = queue_id
