import unittest
from stack_array import Stack


class TestStackArray(unittest.TestCase):

    # Must be setUp() not setup() in order to work
    def setUp(self):
        self.stack = Stack([1, 2, 3])

    def test_push(self):
        # All test here are sequentially dependent
        self.assertEqual(self.stack.push(1), [1, 2, 3, 1])
        self.assertEqual(self.stack.push(5), [1, 2, 3, 1, 5])

    def test_pop(self):
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)

    def test_peek(self):
        self.assertEqual(self.stack.peek(), 3)

    def test_is_empty(self):
        self.assertEqual(self.stack.is_empty(), False)

    def test_all(self):
        self.stack = Stack([4, 5, 6, 7, 8])
        self.assertEqual(self.stack.push(1), [4, 5, 6, 7, 8, 1])
        self.assertEqual(self.stack.pop(), 1)
        self.assertEqual(self.stack.peek(), 8)
        self.assertEqual(self.stack.is_empty(), False)
        self.assertEqual(self.stack.pop(), 8)
        self.assertEqual(self.stack.pop(), 7)
        self.assertEqual(self.stack.peek(), 6)
        self.assertEqual(self.stack.is_empty(), False)


if __name__ == "__name__":
    unittest.main()
