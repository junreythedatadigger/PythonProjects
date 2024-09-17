# Simple Banking System:
#
# Create a Python application that allows users to deposit
# and withdraw money from a bank account. Track balances
# and print a transaction history.
# Skills: Classes, methods, loops, conditionals.

class BankAccount:

    WITHDRAW_WARNING = "Can't process withdrawal! Insufficient balance."
    TRANSACTION_WARNING = "No transaction history!"
    DEPOSIT_TAG = "Deposited"
    WITHDRAW_TAG = "Withdrawn"

    def __init__(self, account_name, account_number, balance):
        self.account_name = account_name
        self.account_number = account_number
        self.__balance = balance
        self.__history = []

    def deposit(self, amount):
        self.__balance += amount
        self.__history.append([self.DEPOSIT_TAG, amount, self.__balance])
        print(f'Deposited: {amount}. New balance: {self.__balance}')
        return self.__balance

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            self.__history.append([self.WITHDRAW_TAG, amount, self.__balance])
            print(f'Withdrawn: {amount}. New balance: {self.__balance}')
            return self.__balance
        else:
            print(self.WITHDRAW_WARNING)
            return self.WITHDRAW_WARNING

    def inquire(self):
        print(f'Current balance: {self.__balance}')
        return self.__balance

    def view_transactions(self):
        if self.__history:
            print('Transaction history')
            for index, item in enumerate(self.__history):
                print(f'{index}: {item[0]}: {item[1]}, New balance: {item[2]}')
            return self.__history
        else:
            print(self.TRANSACTION_WARNING)
            return self.TRANSACTION_WARNING


account = BankAccount('JR Ansing', '111222', 0)

account.inquire()
account.view_transactions()
account.deposit(5000)
account.deposit(1500)
account.withdraw(4500)
account.withdraw(3000)
account.inquire()
account.view_transactions()
account.view_transactions()
account.__balance = 0
account.inquire()