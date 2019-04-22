"""
A list of Car objects all waiting at one side of an intersection and controlled by one traffic light.

The queue module defines a set of states and behaviors associated with a traffic queue. A queue represents
the cars on one street of a traffic light-controlled intersection that are all traveling in the same direction.

A Queue object is iterable

A queue has several attributes:
    - The maximum number of cars the queue can hold (__max_queue_depth variable, default 10)
    - The current state (__state variable, either waiting or moving)
    - The string identifier of the queue (__queue_id variable)
    - The list of cars currently in the queue (__cars list)

Notes
-----
The Queue class is implemented with encapsulated internal state. The four state attributes (__max_queue_depth,
__queue_id, __cars, and __state) are private, exposed via the get_variables() and set_value() methods.

"""

from cars.car import Car
from typing import List


class QueueFullError(TypeError):
    def __init__(self, error_text:str):
        self.__error_text = error_text


class Queue:
    """
    Define a queue of Cars.


    Parameters
    ----------
    queue_id : str
        The identifier name of the queue (required).
    max_queue_depth : int
        The maximum number of Cars in the queue (default 10).

    Attributes
    ----------
    __max_queue_depth : int
        The maximum number of Cars the Queue can hold (default 10).
    __queue_id : str
        The string identifier of the Queue.
    __cars : array_like
        The list of Car instances currently in the Queue
    __state : str
        The current state of the Queue, either 'waiting' or 'moving'. Initial state is 'waiting'.
    """

    def __init__(self, queue_id: str, max_queue_depth: int = 10):
        self.__max_queue_depth = max_queue_depth
        self.__queue_id = queue_id
        self.__cars = []
        self.__index = 0
        self.__state = 'waiting'
        self.__next_queue = self

    def add_car(self, car: Car):
        """
        Add one Car to the Queue.

        Parameters
        ----------
            car : Car
                The Car object to add.

        Returns
        -------
            int
                The number of Cars in the Queue after the add operation.

        Raises
        ------
            QueueFullError
                If the Queue already has max_queue_length Cars in the car[] list.
        """
        if len(self.__cars) < self.__max_queue_depth:
            self.__cars.append(car)
            return len(self.__cars)
        else:
            raise QueueFullError(("Queue '{0}' already full with {1} cars"
                                 ).format(self.__queue_id, len(self.__cars)))

    def fill(self):
        """
        Completely fill this Queue with Cars.

        Returns
        -------
            int
                The number of Cars in the car[] list once filled. Should equal the max_queue_depth variable.
        """
        for _ in range(self.__max_queue_depth):
            self.add_car(Car(queue_id = self.__queue_id))
        return len(self)

    def add_cars(self, cars:List[Car]):
        """
        Add one or more Cars to this Queue.
        """
        for i in range(len(cars)):
            self.add_car(cars[i])
        return len(self.__cars)

    def empty(self):
        """Delete all cars in this Queue."""
        self.__cars = []

    def pop(self, index:int = None):
        """Remove one car from this Queue and return that car to caller."""
        if index:
            return self.__cars.pop(index)
        else:
            return self.__cars.pop()

    def get_variables(self):
        """
        Retrieve the list of variables describing this Queue.

        Returns
        -------
            dict
                The four internal state values, with their name as keys

        Notes
        -----
        This method exists as part of encapsulation of internal variables.
        It works in conjunction with the set_value() method to provide
        method-based access to internal state.
        """
        return {'max_queue_depth': self.__max_queue_depth,
                'queue_id': self.__queue_id,
                'cars': self.__cars,
                'num_cars': len(self),
                'state': self.__state}

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
        if variable == 'max_queue_depth':
            self.__max_queue_depth = my_value
        if variable == 'state':
            self.__state = my_value

    def __str__(self):
        """
        Return a string showing the current state of this queue.

        Returns
        -------
            str
                A formatted, multi-line string with the queue_id, state, cars list, and number of cars.
        """
        return ('Queue {0}:\n\tState: {1}\n'
                '\tMax Depth: {2}\n\tCars: {3}\n\tNum Cars: {4}'
                ).format(self.__queue_id,
                         self.__state,
                         self.__max_queue_depth,
                         self.__cars,
                         str(len(self)))

    def __len__(self):
        """Return the number of cars currently in this queue."""
        return len(self.__cars)

    def __getitem__(self, key: int = 0):
        """Return the Car object at list index key."""
        return self.__cars[key]

    def __iter__(self):
        """Return self as an iterator."""
        return self

    def __next__(self):
        """
        Return next Car object as part of iteration.

        Returns
        -------
            Car
                The next Car object in the list cars.

        Raises
        ------
            StopIteration
                Indicate that the last item in the iterable has been reached.
        """
        try:
            result = self.__cars[self.__index]
        except IndexError:
            raise StopIteration
        self.__index += 1
        return result

    def __contains__(self, item):
        """Return the Car object that matches the item argument."""
        return item in self.__cars

    def is_full(self):
        """Return False if this queue does not have max_queue_depth Cars in it, True otherwise."""
        if len(self) == self.__max_queue_depth:
            return True
        else:
            return False

    def notify(self, can_move: bool):
        """
        Trigger Cars to start moving through the Queue or to stop them.

        Parameters
        ----------
            can_move : bool
                True if Cars are allowed to move (i.e. their light is green), False otherwise.

        Returns
        -------
            str
                The current value of __state.

        Notes
        -----
        Upon invocation, iterate through all Cars in this Queue, telling them they either can or cannot move.
        If the first Car in the Queue reports it has moved 2 spaces (i.e. one car-length), pop() it from the
        Queue.
        """
        if can_move:
            self.__state = 'moving'
        return self.__state, len(self)
