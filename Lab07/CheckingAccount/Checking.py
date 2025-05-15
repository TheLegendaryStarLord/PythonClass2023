#!/usr/bin/env python3
#   Adam Sanchez
#   Cuyamaca College CS-119
#   Lab 7, Exercise 3, classes to determine the checking account

class Checking:
    
    def __init__(self, account_number, customer_name, customer_address, account_balance):
        self.account_number = account_number
        self.customer_name = customer_name
        self.customer_address = customer_address
        self.account_balance = account_balance

    def get_account_number(self):
        return self.account_number

    def set_account_number(self, account_number):
        self.account_number = account_number

    def get_customer_name(self):
        return self.customer_name

    def set_customer_name(self, customer_name):
        self.customer_name = customer_name

    def get_customer_address(self):
        return self.customer_address

    def set_customer_address(self, customer_address):
        self.customer_address = customer_address

    def get_account_balance(self):
        return self.account_balance

    def set_account_balance(self, account_balance):
        self.account_balance = account_balance
        
    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
        else:
            print("Insufficient funds to be withdrawn")
        
    def deposit(self, amount):
        self.account_balance += amount

    def to_string(self):
        return f"Account Number: {self.account_number}\nCustomer Name: {self.customer_name}\nCustomer Address: {self.customer_address}\nAccount Balance: ${self.account_balance:.2f}"