import unittest
import number_21_game as n2g


class TestNumber21Game(unittest.TestCase):

    def test_select_order(self):
        self.assertEqual(n2g.select_order(1), "You")
        self.assertEqual(n2g.select_order(2), "Computer")
        self.assertEqual(n2g.select_order(3), "Incorrect choice!")

    def test_enter_numbers(self):
        self.assertEqual(n2g.enter_numbers(0, "1,2,3", ), [1, 2, 3])
        self.assertEqual(n2g.enter_numbers(0, "1,2,4"), "Numbers not in sequence")
        self.assertEqual(n2g.enter_numbers(0, "1,,2"), "Invalid inputs")
        self.assertEqual(n2g.enter_numbers(0, "1,2,,4"), "Invalid inputs")
        self.assertEqual(n2g.enter_numbers(1, "1,2,,4"), "Invalid inputs")
        self.assertEqual(n2g.enter_numbers(2, "3,2,1"), "Numbers not in sequence")
        self.assertEqual(n2g.enter_numbers(1, "3,2,1"), "Should start at 2")
        self.assertEqual(n2g.enter_numbers(0, "1,2,3,4"), "Numbers exceeds 3 inputs")

    def test_computer_turn(self):
        self.assertEqual(n2g.computers_turn(0, 2), [1, 2])
        self.assertEqual(n2g.computers_turn(1, 3), [2, 3, 4])
        self.assertEqual(n2g.computers_turn(12, 3), [13, 14, 15])


if __name__ == "__name__":
    unittest.main()
