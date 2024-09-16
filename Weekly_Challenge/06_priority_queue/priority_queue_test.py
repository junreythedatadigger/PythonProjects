import unittest
from priority_queue import PriorityQueue

class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        self.pq = PriorityQueue([1, 3, 5, 7, 9])
        self.assertEqual(self.pq.add_value(4), [1, 3, 4, 5, 7, 9])  # add assertion here

    def test_case_2(self):
        self.pq = PriorityQueue([])
        self.assertEqual(self.pq.add_value(1), [1])


if __name__ == '__main__':
    unittest.main()
