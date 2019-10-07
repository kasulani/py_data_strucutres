import unittest
from linked_list.list import SingleNode, DoubleNode


class TestSingleNode(unittest.TestCase):
    """ TEST THE SINGLE NODE CLASS """

    def setUp(self):
        self._node_value = 34
        self._next_value = 35
        self._node = SingleNode(self._node_value)
        self._node.next = SingleNode(self._next_value)

    def test_node_value(self):
        """ This test ensures that the value of the node is set """
        self.assertEqual(self._node.data, self._node_value)

    def test_next_attribute_of_node(self):
        """ This test ensures that the next attribute of the node points to another node """
        self.assertIsInstance(self._node.next, SingleNode)
        self.assertEqual(self._node.next.data, self._next_value)
        with self.assertRaises(TypeError) as ctx:
            self._node.next = 2
        self.assertEqual(str(ctx.exception), "value is not of type BaseNode")


class TestDoubleNode(unittest.TestCase):
    """ TEST THE DOUBLE NODE CLASS """

    def setUp(self):
        self._node_value = 10
        self._next_value = 11
        self._prev_value = 9
        self._node = DoubleNode(self._node_value)
        self._node.next = DoubleNode(self._next_value)
        self._node.previous = DoubleNode(self._prev_value)

    def test_node_value(self):
        """ This test ensures that the value of the double node is set """
        self.assertEqual(self._node.data, self._node_value)

    def test_next_attribute_of_node(self):
        """ This test ensures the next attribute of node points to another node instance """
        self.assertIsInstance(self._node.next, DoubleNode)
        self.assertEqual(self._node.next.data, self._next_value)

    def test_precious_attribute_of_node(self):
        """ This test ensures the previous attribute of node points to another node instance """
        self.assertIsInstance(self._node.previous, DoubleNode)
        self.assertEqual(self._node.previous.data, self._prev_value)
