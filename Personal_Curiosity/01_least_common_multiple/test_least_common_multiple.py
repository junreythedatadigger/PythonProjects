import unittest
from least_common_multiple import lcm_func


class TestLeastCommonMultiple(unittest.TestCase):
    def test_lcm_func(self):
        self.assertEqual(lcm_func(2, 4), 4)
        self.assertEqual(lcm_func(4, 2), 4)
        self.assertEqual(lcm_func(4, 6), 12)
        self.assertEqual(lcm_func(4, 4), 4)
        self.assertEqual(lcm_func(8, 12), 24)
        self.assertEqual(lcm_func(1, 2), 2)
        self.assertEqual(lcm_func(12, 15), 60)

if __name__ == '__main__':
    unittest.main()