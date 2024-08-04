import unittest
from greatest_common_factor import gcf_func

class TestGreatestCommonFactor(unittest.TestCase):
    def test_gcf_func(self):
        self.assertEqual(gcf_func(4,6), 2)
        self.assertEqual(gcf_func(4, 8), 4)
        self.assertEqual(gcf_func(4, 4), 4)
        self.assertEqual(gcf_func(12, 15), 3)
        self.assertEqual(gcf_func(12, 20), 4)
        self.assertEqual(gcf_func(45, 60), 15)

if __name__ == "__name__":
    unittest.main()