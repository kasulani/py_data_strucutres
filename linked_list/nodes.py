"""
    Data Structures in python
    10-May-2018
    Emmanuel.King.Kasulani

    LINKED LIST NODES
"""


class BaseNode(object):

    def __init__(self, _data=None):
        self._data = _data  # holds data
        self._next = None  # points to the next node

    def __str__(self):
        return "{}".format(self.data)

    def __repr__(self):
        return "Node <data: {} - next: {}>".format(self._data, self._next)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, _data):
        self._data = _data

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, node):
        if isinstance(node, BaseNode):
            self._next = node
            return
        raise TypeError("value is not of type BaseNode")


class SingleNode(BaseNode):
    """ The Node class is the basic building block of a singly linked list """
    pass


class DoubleNode(SingleNode):
    """ The Double Node is the basic building block for a doubly linked list """

    def __init__(self, _data=None):
        super().__init__(_data)
        self._previous = None  # points to the previous node

    def __repr__(self):
        return "Node <data: {} - next: {} - prev: {}>".format(self._data, self._next, self._previous)

    @property
    def previous(self):
        return self._previous

    @previous.setter
    def previous(self, node=None):
        if isinstance(node, BaseNode):
            self._previous = node
            return
        raise TypeError("value is not of type BaseNode")
