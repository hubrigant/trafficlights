"""
A list of Car objects all waiting at one side of an intersection and controlled
by one traffic light.

The queue module defines a set of states and behaviors associated with a
traffic queue. A queue represents the cars on one street of a traffic
light-controlled intersection that are all traveling in the same direction.

A Queue object is iterable

A queue has several attributes:
    - The maximum number of cars the queue can hold (__max_queue_depth variable
      default 10)
    - The current state (__state variable, either waiting or moving)
    - The string identifier of the queue (__queue_id variable)
    - The list of cars currently in the queue (__cars list)

Notes
-----
The Queue class is implemented with encapsulated internal state. The four
state attributes (__max_queue_depth, __queue_id, __cars, and __state) are
private, exposed via the get_variables() and set_value() methods.

"""

from typing import List


class Stoplight:
    """
    Define a Stoplight that controls the flow of Cars between one or more
    Queues.


    Parameters
    ----------
    in_queues : array_like
        The list of input queues (required).
    out_queues : array_like
        The list of output queues (required).

    Attributes
    ----------
    __max_queue_depth : int
        The maximum number of Cars the Queue can hold (default 10).
    __queue_id : str
        The string identifier of the Queue.
    __cars : array_like
        The list of Car instances currently in the Queue
    __state : str
        The current state of the Queue, either 'waiting' or 'moving'. Initial
        state is 'waiting'.
    """

    def __init__(self, in_queues: List, out_queues: List):
        print("init> Before assigns")
        self.__in_queues = []
        self.__out_queues = []
        self.__in_queues = in_queues
        self.__out_queues = out_queues

    def num_inputs(self):
        return len(self.__in_queues)

    def num_outputs(self):
        return len(self.__out_queues)
