class car:
    'Defines a single car with its queue status and wait time'
    def __init__(self, queue_id, queue_position):
        self.queue_id = queue_id
        self.queue_position = queue_position
        self.time_waiting = 0
        self.total_cars_waiting += 1


    def change_queues(self):
        if self.queue_id == 'left side':
            self.queue_id = 'left funnel'
            self.queue_position = left_funnel_cars_waiting

