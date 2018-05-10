"""
    Data Structures in python
    18-April-2018
    Emmanuel.King.Kasulani

    LINKED LISTS
"""

from collections.abc import Collection


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
        self._next = node


class SingleNode(BaseNode):
    """ The Node class is the basic building block of a singly linked list """
    pass


class DoubleNode(BaseNode):
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
        self._previous = node


class LinkedList(Collection):
    """ This is a singly linked list """

    def __init__(self):
        self._head = None
        self._tail = None
        self._count = 0

    def __contains__(self, item):
        """
        This method checks for if an item is in the chain of nodes
        that are part of a linked list collection
        """
        node = self._head
        found = False
        while node is not None:
            if node.data == item:
                found = True
            node = node.next
        return found

    def __len__(self):
        return self._count

    def __iter__(self):
        """
        This method allows this collection to be used in for loops
        """
        node = self._head
        while node is not None:
            # yield the data stored by the node
            yield node.data
            # reassign node to point the next attribute
            node = node.next

    def __str__(self):
        return "<head:{}>".format(self._head)

    def __repr__(self):
        return "<head: {} - tail: {}>".format(self._head, self._tail)

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    def add(self, item, add_to_front=True):
        """ Adds item, to the front by default, of the collection """
        if self._count > 0:
            if add_to_front:
                temp = self._head  # assign the current head to a temporary variable
                self._head = SingleNode(item)  # assign the new item node as the head node
                self._head.next = temp  # point the next attribute of the new head node to the temp node
            else:
                # add to the end of the collection
                temp = self._tail  # assign the current tail to a temporary variable
                self._tail = SingleNode(item)  # assign the new item node as the tail node
                temp.next = self._tail  # point the next attribute of temp node to the new tail node

        else:
            # this block of code will execute only once, i.e when count is 0
            self._head = SingleNode(item)
            # At the start of the chain, the head and tail point to the same item
            self._tail = self._head
        self._count += 1

    def remove_first_item(self):
        """ Removes the first item in the chain of nodes """
        if self._count > 0:
            temp = self._head.next
            self._head = temp
            self._count -= 1
        else:
            raise ValueError("list is empty")

    def remove_last_item(self):
        """ Removes the last item in the chain of nodes """
        # this operation is O(n)
        if self._count > 0:
            node = self._head  # move the pointer to the head
            temp = None  # holds the node before tail node
            while node != self._tail:
                temp = node  # save the node before moving on to the next node in the chain
                node = node.next
            self._tail = temp  # this is the last node saved before reaching the tail
            self._tail.next = None  # remove the previous pointer to the previous tail
            self._count -= 1
        else:
            raise ValueError("list is empty")

    def remove_item(self, item):
        if self._count > 0:
            node = self._head
            prev = None  # previous node in the chain
            found = False
            while node is not None:
                if node.data == item:  # item has been found
                    found = True
                    if node == self._head: # handle case where the node is the head
                        temp = self._head.next
                        self._head = temp
                    elif node == self._tail: # handle case where the node is the tail
                        prev.next = None
                        self._tail = prev
                    else: # handle the case when the node is in the middle
                        prev.next = node.next
                    break
                prev = node
                node = node.next
                self._count -= 1
            if not found:
                raise ValueError("item {} not found".format(item))


class DoublyLinkedList(object):
    """ This is a doubly linked list """
    pass

