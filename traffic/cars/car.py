"""
Defines a single car with its traffic-related state.

The car module defines the attributes and behaviors of a car as it moves through traffic.
For purposes of the traffic light timing simulation, all cars are presumed to move at the
same rate (1 unit per iteration cycle, where 1 car length == 2 units). Each car has its
own latency, which is the measure of how many cycles pass between when the car is notified
that it is allowed to move and when it actually begins moving.

Notes
-----
The Car class is implemented with encapsulated internal state. The six state attributes
(__queue_id, __latency, __time_waiting, __distance_moved, __last_distance_moved, and
__state) are private, exposed via the get_variables() and set_value() methods.

"""

import random


class Car:
    """
    A single car.

    Parameters
    ----------
    queue_id : str
        The queue identifier of the Queue the Car is currently in.

    Attributes
    ----------
        __queue_id : str
            The identifier string of the queue the Car is currently in.
        __latency : int
            How many iteration cycles elapse between when the Car is
            notified it is able to move until when the Car actually
            begins to move. The value is randomly determined, in a range of
            2 through 7, each time the Car transitions from "waiting" to
            "reacting" state.
        __time_waiting : int
            How many iteration cycles have elapsed from when the simulation
            started and when the Car exits all of the queues in its path.
        __state : str
            The movement state the Car is currently in. Allowed values are
            "waiting", "reacting", and "moving".
        __distance_moved : int
            How many units the Car moved this cycle.
        __last_distance_moved : int
            How many units the Car moved the previous cycle.
    """

    def __init__(self, queue_id: str):
        self.__queue_id = queue_id
        self.__latency = 0
        self.__time_waiting = 0
        self.__state = 'waiting'
        self.__distance_moved = 0
        self.__last_distance_moved = 0

    def set_value(self, variable: str, value: str, type: str):
        """
        In order to prevent direct modification of class variables, this method
        works in conjunction with the get_variable() method to provide
        method-based access to internal state.

        Parameters
        ----------
            variable : string
                The name of the variable to be set, minus the leading underscores
            value : str
                The value to be set
            type : str
                What type the value is to be cast to (if any)
        """
        if type == 'int':
            my_value = int(value)
        else:
            my_value = value
        if variable == 'queue_id':
            self.__queue_id = my_value
            return self.__queue_id
        if variable == 'latency':
            self.__latency = my_value
            return self.__latency
        if variable == 'time_waiting':
            self.__time_waiting = my_value
            return self.__time_waiting
        if variable == 'state':
            self.__state = my_value
            return self.__state
        if variable == 'distance_moved':
            self.__distance_moved = my_value
            return self.__distance_moved
        if variable == 'last_distance_moved':
            self.__last_distance_moved = my_value
            return self.__last_distance_moved

    def __str__(self):
        """
        Return a string showing the current state of this queue.

        Returns
        -------
            str
                A formatted, multi-line string with the queue_id, state, latency,
                distance_moved, last_distance_moved, and time_waiting.
        """
        return ('Queue ID: {0}; State: {1}, Latency: {2}, Moved: {3}, '
                'Waiting: {4}, Last Moved: {5}'
               ).format(self.__queue_id,
                        self.__state,
                        self.__latency,
                        self.__distance_moved,
                        self.__time_waiting,
                        self.__last_distance_moved
                        )

    def get_variables(self):
        """
        Retrieve the list of variables describing this Car.

        Returns
        -------
            dict
                The six internal state values, with their name as keys

        Notes
        -----
        This method exists as part of encapsulation of internal variables.
        It works in conjunction with the set_value() method to provide
        method-based access to internal state.
        """
        return {'latency': self.__latency,
                'state': self.__state,
                'queue_id': self.__queue_id,
                'distance_moved': self.__distance_moved,
                'time_waiting': self.__time_waiting,
                'last_distance_moved': self.__last_distance_moved
               }

    def notify(self, can_move: str):
        """
        Trigger a Car to transition into or out of the "waiting" state.

        Parameters
        ----------
        can_move : bool
            True if allowed to move, False otherwise.

        Returns
        -------
        A tuple of the Car's current state, it's last_distance_moved, and
        its current distance_moved.
        """
        self.__time_waiting += 1
        if can_move:
            if self.__state == 'waiting':
                self.__state = 'reacting'
                self.__latency = random.randrange(2, 7)
            elif self.__state == 'reacting':
                if self.__latency > 0:
                    self.__latency -= 1
                else:
                    self.__state = 'moving'
                    self.__last_distance_moved = self.__distance_moved
                    self.__distance_moved += 1
            elif self.__state == 'moving':
                self.__last_distance_moved = self.__distance_moved
                self.__distance_moved += 1
        else:
            self.__state = 'waiting'
        return self.__state, self.__last_distance_moved, self.__distance_moved
