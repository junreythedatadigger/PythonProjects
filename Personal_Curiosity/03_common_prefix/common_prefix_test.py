import unittest
from common_prefix import get_common_prefix

class TestCommonPrefix(unittest.TestCase):

    def test_common_prefix(self):
        self.assertEqual(get_common_prefix("compare","compute"),"comp")
        self.assertEqual(get_common_prefix("avail","avoid"),"av")
        self.assertEqual(get_common_prefix("able","table"),"")
        self.assertEqual(get_common_prefix("hated","hatred"),"hat")


if __name__ == '__name__':
    unittest.main()