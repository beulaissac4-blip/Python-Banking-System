
from abc import ABC, abstractmethod


# Abstract Parent Class
class BankAccount(ABC):

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
        self.transactions = []

    def display(self):
        print("Account Holder:", self.name)
        print("Balance:", self.__balance)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.transactions.append("Deposited: " + str(amount))
            print("Amount Deposited Successfully!")
        else:
            print("Invalid Amount!")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            self.transactions.append("Withdrawn: " + str(amount))
            print("Amount Withdrawn Successfully!")
        else:
            print("Insufficient Balance or Invalid Amount!")

    def show_history(self):
        print("\nTransaction History:")
        for transaction in self.transactions:
            print(transaction)

    @abstractmethod
    def account_type(self):
        pass


# Child Class 1
class SavingsAccount(BankAccount):

    def account_type(self):
        print("This is a Savings Account")


# Child Class 2
class CurrentAccount(BankAccount):

    def account_type(self):
        print("This is a Current Account")


# Creating Objects
account1 = SavingsAccount("Beula", 1000)
account2 = CurrentAccount("Priya", 2000)


# Display Account Types
account1.account_type()
account2.account_type()


# Deposit and Withdraw
account1.deposit(500)
account1.withdraw(200)

account1.display()
account1.show_history()
