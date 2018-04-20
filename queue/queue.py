"""
    Data Structures in python
    18-April-2018
    Emmanuel.King.Kasulani

    QUEUE
"""
import abc


class AbstractQueue(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def _update_count(self):
        pass

    @abc.abstractmethod
    def enqueue(self, item):
        pass

    @abc.abstractmethod
    def dequeue(self):
        pass

    @abc.abstractmethod
    def peek(self):
        pass

    @property
    @abc.abstractmethod
    def count(self):
        pass


class BaseQueue(AbstractQueue):
    """ QUEUE BASE CLASS """

    def __init__(self):
        self._items = []
        self._count = 0

    def _update_count(self):
        """
        The method update the count variable with the current
        item count in the stack
        """
        self._count = len(self._items)

    def enqueue(self, item):
        pass

    def dequeue(self):
        """
        This method removes an item from the queue
        """
        try:
            item = self._items.pop()
            # This operation decrements the number of items
            # in the queue, we need to update the count variable
            self._update_count()
            return item
        except IndexError:
            raise IndexError("Queue is empty")

    def peek(self):
        """
        This method returns the top most item in the queue
        """
        if self._count == 0:
            raise IndexError("Queue is empty")
        return self._items[self._count - 1]

    @property
    def count(self):
        """
        This method returns current count of items in the queue
        """
        return self._count


class Queue(BaseQueue):
    """
    Queue class implemented using Lists in Python
    """

    def enqueue(self, item):
        """
        This method adds an item to the queue
        """
        self._items.insert(0, item)
        # This operation increments the number of items
        # in the queue, we need to update the count variable
        self._update_count()


class PriorityQueue(BaseQueue):
    """
    Priority Queue class implemented using Lists in Python
    """

    def enqueue(self, item):
        if self._count > 0:
            position = self._count
            for _item in reversed(self._items):
                if item < _item:
                    self._items.insert(position, item)
                    # This operation increments the number of items
                    # in the queue, we need to update the count variable
                    self._update_count()
                    return None
                position -= 1
        self._items.insert(0, item)
        self._update_count()
