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
    duration : int
        The amount of time an input queue is allowed to flow its Cars (required).

    Attributes
    ----------
    __in_queues : array_like
        The list of input queues
    __out_queues : array_like
        The list of output queues
    __duration : int
        The amount of time a given input queue is allowed to flow its Cars.

    Notes
    -----
    A Stoplight object is the mediating layer that controls the flow of Cars from
    one or more input Queues (a.k.a. street lanes) and one or more output Queues.
    It can be thought of as a model of a real-world stoplight, or in the case of
    a one input, one output object, a gate.

    The Stoplight object has a duration value that determines how many cycles a
    given Queue is allowed to flow Cars.
    """

    def __init__(self, in_queues: List, out_queues: List, duration: int):
        self.__in_queues = []
        self.__out_queues = []
        self.__in_queues = in_queues
        self.__out_queues = out_queues
        self.__duration = duration

    def num_inputs(self):
        return len(self.__in_queues)

    def num_outputs(self):
        return len(self.__out_queues)

    def duration(self):
        return self.__duration
