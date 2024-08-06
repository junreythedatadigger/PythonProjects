import unittest
import word_guessing as wg

class TestWordGuessing(unittest.TestCase):

    def test_validate_guessing(self):
        self.assertEqual(wg.validate_guess(
            "sample", "******", "a"),
            ("*a****", True))
        self.assertEqual(wg.validate_guess(
            "sample", "*a****", "e"),
            ("*a***e", True))
        self.assertEqual(wg.validate_guess(
            "sample", "*a***e", "b"),
            ("*a***e", False))
        # self.assertEqual(wg.validate_guess("Sample", "s"),"s*****")
        # self.assertEqual(wg.validate_guess("alphabet", "a"), "a***a***")
        self.assertEqual(wg.validate_guess("separate", "********", "b"), ("********",False))
        # self.assertEqual(wg.validate_guess("mississippi", "s"), "**ss*ss****")
        # self.assertEqual(wg.validate_guess("Hello World!", "l"), "**ll* ***l**")

    def test_print_blank_word(self):
        self.assertEqual(wg.print_blank_word("sample"), "******")
        self.assertEqual(wg.print_blank_word("Hello World!"), "***** ******")

    def test_get_unique_letters(self):
        self.assertEqual(wg.get_unique_letters("sample"),"aelmps")
        self.assertEqual(wg.get_unique_letters("availability"),"abiltvy")

    # def test_show_matched_letters(self):
    #     self.assertEqual(wg.show_matched_letters("a",[0,3],"a**a"))

if __name__ == "__name__":
    unittest.main()