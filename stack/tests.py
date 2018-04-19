import unittest
from .stack import Stack


class TestStack(unittest.TestCase):

    def setUp(self):
        self.test_item = 8
        self.expected_count = 5
        self.expected_top_item = 7
        self.stack = Stack(init_items=[3, 4, 5, 6, 7])

    def test_push(self):
        """
        This test ensures that the push operation in setup
        has the stack count incremented to 6 items
        """
        self.stack.push(self.test_item)
        self.assertEqual(self.stack.count, self.expected_count + 1)

    def test_pop(self):
        """
        This test ensures that the push operation in setup
        has the stack count decrements to 4 items
        """
        self.assertEqual(self.stack.pop(), 7)
        self.assertEqual(self.stack.count, self.expected_count - 1)
        # create an empty stack
        stack = Stack()
        # assert that an exception raised when pop operation is done
        # on an empty stack
        self.assertRaises(IndexError, lambda: stack.pop())

    def test_peek(self):
        """
        This test ensures that the peek operation returns the
        top item in the stack which corresponds to 7 as initialized
        in setup
        """
        self.assertEqual(self.stack.peek(), self.expected_top_item)
        # create an empty stack
        stack = Stack()
        # assert that an exception raised when peek operation is done
        # on an empty stack
        self.assertRaises(IndexError, lambda: stack.peek())


if __name__ == '__main__':
    unittest.main()