# project 1
# Bank account class

class BankAccount:

    """
    A lass to represent a bank account.

    """

    def __init__(self, name, balance):

        """
        initialize the bank account with name and balance
        """
        self.name = name
        self.__balance = balance

    # define a getter method the balance

    def get_balance(self):
        return self.__balance

    def withdraw(self, amount):
        if self.__balance > 0 and amount > 0:
            self.__balance -= amount
        else:
            print("please try again!")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Please add an amount")



