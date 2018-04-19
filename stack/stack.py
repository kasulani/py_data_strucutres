"""
    Data Structures in python
    17-April-2018
    Emmanuel.King.Kasulani

    STACK
"""


class Stack(object):
    """
    Stack class implemented using Lists in Python
    """
    def __init__(self, init_items=None):
        self._items = [] if init_items is None else init_items
        self._count = 0 if self._items is None else len(self._items)

    def _update_count(self):
        """
        The method update the count variable with the current
        item count in the stack
        """
        self._count = len(self._items)

    def push(self, item):
        """
        This method adds an item to the stack
        """
        self._items.append(item)
        # This operation increments the number of items
        # in the stack, we need to update the count variable
        self._update_count()

    def pop(self):
        """
        This method removes an item from the stack
        """
        try:
            item = self._items.pop()
            # This operation decrements the number of items
            # in the stack, we need to update the count variable
            self._update_count()
            return item
        except IndexError:
            raise IndexError("Stack is empty")

    def peek(self):
        """
        This method returns the top most item in the stack
        """
        if self._count == 0:
            raise IndexError("Stack is empty")
        return self._items[self._count-1]

    @property
    def count(self):
        """
        This method returns current count of items in the stack
        :return:
        """
        return self._count
