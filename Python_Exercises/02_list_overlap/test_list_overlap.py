# Test case script for list overlap

import unittest
from list_overlap import list_overlap_func

class TestListOverlap(unittest.TestCase):

    def test_list_overlap_func(self):
        self.assertEqual(list_overlap_func([1,2,3,4,1,2,3,4],[3,4,4,5,6,1,2,2]),[1,2,2,3,4,4])
        self.assertEqual(list_overlap_func([1,2,3,4],[3,4,5,6]),[3,4])
        self.assertEqual(list_overlap_func(
            [1,2,3,4,1,2,3,4],
            [3,4,5,6,1,2,3]),
            [1,2,3,3,4])
        self.assertEqual(list_overlap_func(
            [1,2,3,4,1,2,3,4],
            [1,2,2,3,3,4,4,5]),
            [1,2,2,3,3,4,4])


if __name__ == '__main__':
    unittest.main(verbosity=2)