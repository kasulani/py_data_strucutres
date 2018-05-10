import unittest
from linked_list.list import LinkedList


class TestLinkedList(unittest.TestCase):
    """ Test Linked List collection """

    def setUp(self):
        self._linked_list = LinkedList()
        for i in range(3):
            self._linked_list.add(i+1)

    def test_iterator(self):
        """
        This test ensures that the collection returns an iterator that can be used in for loops
        """
        iterator = iter(self._linked_list)

        self.assertEqual(next(iterator), 3)
        self.assertEqual(next(iterator), 2)
        self.assertEqual(next(iterator), 1)
        self.assertRaises(StopIteration, lambda: next(iterator))

    def test_add_to_the_front(self):
        """
        This test ensures that when an item is added at the end of the linked list, the head points
        to this item
        """
        self.assertEqual(self._linked_list.head.data, 3)  # this is the last item added to the collection
        self.assertEqual(self._linked_list.tail.data, 1)  # this is the first item added to the collection
        self.assertEqual(len(self._linked_list), 3)

    def test_add_to_the_end(self):
        """
        This test ensures that when an item is added at the end of the linked list, the tail points
        to this item
        """
        self._linked_list.add(4, add_to_front=False)  # new item
        self.assertEqual(self._linked_list.head.data, 3)  # this is the last item added to the collection
        self.assertEqual(self._linked_list.tail.data, 4)  # this is the new item added the end of the collection
        self.assertEqual(len(self._linked_list), 4)  # size of the list increments by 1

    def test_remove_first_item(self):
        """
        This test ensures that when the first item in the linked list is removed, the head is updated to
        point to the next item in the collection
        """
        self._linked_list.remove_first_item()
        self.assertEqual(self._linked_list.head.data, 2)
        self.assertEqual(self._linked_list.tail.data, 1)

        iterator = iter(self._linked_list)

        self.assertEqual(next(iterator), 2)
        self.assertEqual(next(iterator), 1)
        self.assertRaises(StopIteration, lambda: next(iterator))

        self.assertEqual(len(self._linked_list), 2)

    def test_remove_last_item(self):
        """
        This test ensures that when the last item in the linked list is removed, the tail is updated to
        point to the previous item in the collection
        """
        self._linked_list.remove_last_item()
        self.assertEqual(self._linked_list.head.data, 3)
        self.assertEqual(self._linked_list.tail.data, 2)

        iterator = iter(self._linked_list)

        self.assertEqual(next(iterator), 3)
        self.assertEqual(next(iterator), 2)
        self.assertRaises(StopIteration, lambda: next(iterator))

        self.assertEqual(len(self._linked_list), 2)

    def test_remove_item(self):
        """
        This test ensures that when a specific item in the collection can be removed if it exists
        """
        self._linked_list.remove_item(1)
        self.assertFalse(1 in self._linked_list)

    def test_remove_first_and_last_item_from_empty_list(self):
        """
        This test ensures that when remove item is invoked on an empty list, an exception is raise
        """
        linked_list = LinkedList()
        self.assertRaises(ValueError, lambda: linked_list.remove_first_item())
        self.assertRaises(ValueError, lambda: linked_list.remove_last_item())

    def test_raises_exception_on_removing_a_non_existing_item(self):
        """
        This tests ensures that an exception is raised when an attempt to remove a non existing item in
        the collection is invoked
        """
        with self.assertRaises(ValueError):
            self._linked_list.remove_item(100)
