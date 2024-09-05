import unittest
from anagram_strings import is_anagram


class TestAnagramStrings(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(is_anagram("123", "123"), True)
        self.assertEqual(is_anagram("123", "124"), False)

    def test_case_2(self):
        self.assertEqual(is_anagram("123", "132"), True)
        self.assertEqual(is_anagram("center", "centre"), True)
        self.assertEqual(is_anagram("center", "Centre"), True)
        self.assertEqual(is_anagram("live", "evil"), True)
        self.assertEqual(is_anagram("amble", "BLAME"), True)
        self.assertEqual(is_anagram("angered", "enraged"), True)

    def test_case_3(self):
        self.assertEqual(is_anagram("A decimal point", "I'm a dot in place"), True)
        self.assertEqual(is_anagram("parliament", "partial men"), True)
        self.assertEqual(is_anagram("Clint Eastwood", "Old West Action"), True)
        self.assertEqual(is_anagram("Eleven plus two", "Twelve plus one"), True)
        self.assertEqual(is_anagram("The American fast-food giant McDonald’s",
                                    "Digest a ton of fat and random chemicals"), True)


if __name__ == '__main__':
    unittest.main()
