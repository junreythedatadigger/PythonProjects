import unittest
import word_guessing as wg

class TestWordGuessing(unittest.TestCase):

    def test_check_guessing(self):
        self.assertEqual(wg.check_guess("sample", "a"),[1])
        self.assertEqual(wg.check_guess("Sample", "s"),[0])
        self.assertEqual(wg.check_guess("alphabet", "a"), [0,4])
        self.assertEqual(wg.check_guess("separate", "a"), [3,5])
        self.assertEqual(wg.check_guess("mississippi", "s"), [2,3,5,6])
        self.assertEqual(wg.check_guess("Hello World!", "l"), [2,3,9])

    def test_print_blank_word(self):
        self.assertEqual(wg.print_blank_word("sample"), "******")
        self.assertEqual(wg.print_blank_word("Hello World!"), "************")



if __name__ == "__name__":
    unittest.main()