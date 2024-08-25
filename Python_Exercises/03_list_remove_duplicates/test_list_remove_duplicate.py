# 1,2,3,4,1,2,2,2,2,3,3,4,5,5,6,6,7,8,9,7,5,4

import unittest
from list_remove_duplicate import list_remove_duplicate_func

class TestListRemoveDuplicate(unittest.TestCase):

    def test_list_remove_duplicate_func(self):
        self.assertEqual(list_remove_duplicate_func(
            [1,2,3,4,1,2,2,2,2,3,3,4,5,5,6,6,7,8,9,7,5,4]),
            [1,2,3,4,5,6,7,8,9])
        self.assertEqual(list_remove_duplicate_func(
            [1,2,3,4,5,1,2,3,4,5,6,1,2,3,4,5,6,7,8,9,0,9,8,7,6,5,4,3,2,1]),
            [0,1,2,3,4,5,6,7,8,9])


if __name__ == '__main__':
    unittest.main(verbosity=2)