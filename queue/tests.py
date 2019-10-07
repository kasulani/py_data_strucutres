import unittest
from .queue import Queue, PriorityQueue


class TestQueue(unittest.TestCase):

    def setUp(self):
        self._queue = Queue()
        self._expected_count = 4
        self.expected_top_item = 1
        for i in range(1, 5):
            self._queue.enqueue(i)

    def test_enqueue(self):
        self._queue.enqueue(5)
        self.assertEqual(self._queue.count, self._expected_count + 1)

    def test_dequeue(self):
        self.assertEqual(self._queue.dequeue(), 1)
        self.assertEqual(self._queue.count, self._expected_count - 1)

    def test_peek(self):
        self.assertEqual(self._queue.peek(), 1)


class TestPriorityQueue(unittest.TestCase):

    def setUp(self):
        self._queue = PriorityQueue()
        self._expected_count = 6
        self.expected_top_item = 1

    def test_priority_queue(self):
        self._queue.enqueue(5)
        self._queue.enqueue(3)
        self._queue.enqueue(4)
        self._queue.enqueue(0)  # this should be the first item out
        self._queue.enqueue(1)
        self._queue.enqueue(2)

        self.assertEqual(self._queue.count, self._expected_count)
        self.assertEqual(self._queue.peek(), 0)
        self.assertEqual(self._queue.dequeue(), 0)
        self.assertEqual(self._queue.count, self._expected_count - 1)
