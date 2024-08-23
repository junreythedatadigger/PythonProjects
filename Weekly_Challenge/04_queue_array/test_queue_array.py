import unittest
from queue_array import Queue


class TestQueueArray(unittest.TestCase):
    def test_queue(self):
        self.queue = Queue([1, 2, 3, 4])
        self.assertEqual(self.queue.is_empty(), False)
        self.assertEqual(self.queue.remove(), 1)
        self.assertEqual(self.queue.reverse(), [4, 3, 2])


if __name__ == '__main__':
    unittest.main()
