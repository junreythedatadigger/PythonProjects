import unittest
from factorization import factorize

class TestFactorzation(unittest.TestCase):
    def test_factorization(self):

        self.assertEqual(factorize(4), [2,2])
        self.assertEqual(factorize(6), [2,3])
        self.assertEqual(factorize(1), [])
        self.assertEqual(factorize(30), [2,3,5])
        self.assertEqual(factorize(100), [2,2,5,5])
        self.assertEqual(factorize(60), [2,2,3,5])


if __name__ == "__name__":
    unittest.main()