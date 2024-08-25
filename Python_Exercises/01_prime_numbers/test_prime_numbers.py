# Test case script for prime_number.py

import unittest
import prime_numbers

class TestPrimeNumbers(unittest.TestCase):

    def test_list_prime_numbers(self):
        self.assertEqual(prime_numbers.list_prime_number(2),'2')
        self.assertEqual(prime_numbers.list_prime_number(4),'2, 3')
        self.assertEqual(prime_numbers.list_prime_number(0),"No prime number(s)")
        self.assertEqual(prime_numbers.list_prime_number(-2),"No prime number(s)")

if __name__ == '__main__':
    unittest.main(verbosity=2)