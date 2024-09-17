import unittest
from simple_banking_system import BankAccount


class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        self.account = BankAccount('JR Ansing', '000111222333', 0)
        self.assertEqual(self.account.deposit(100), 100)
        self.assertEqual(self.account.inquire(), 100)
        self.assertEqual(self.account.deposit(100),200)
        self.assertEqual(self.account.inquire(),200)

    def test_case_2(self):
        self.account = BankAccount('JR','0011', 2000)
        self.assertEqual(self.account.withdraw(3000), self.account.WITHDRAW_WARNING)
        self.assertEqual(self.account.deposit(1000), 3000)
        self.assertEqual(self.account.view_transactions(),[[self.account.DEPOSIT_TAG, 1000, 3000]])
        self.assertEqual(self.account.withdraw(1500), 1500)
        self.assertEqual(self.account.view_transactions(), [[self.account.DEPOSIT_TAG, 1000, 3000], [self.account.WITHDRAW_TAG, 1500, 1500]])


if __name__ == '__main__':
    unittest.main()
