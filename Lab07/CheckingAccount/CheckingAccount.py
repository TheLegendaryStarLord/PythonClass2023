#!/usr/bin/env python3
#   Adam Sanchez
#   Cuyamaca College CS-119
#   Lab 7, Exercise 3, use classes checking account

from Checking import Checking

account_number = input("\n\tEnter your account number: ")
customer_name = input("\n\tEnter the name on your account: ")
customer_address = input("\n\tEnter the address on this account: ")
initial_balance = float(input("\n\tEnter your inital balance: "))

account = Checking(account_number, customer_name, customer_address, initial_balance)

print(account.to_string())

withdraw_amount = float(input("\nHow much would you like to withdraw: "))
account.withdraw(withdraw_amount)
print("\n\tAmount withdrawn.")

print(account.to_string())

deposit_amount = float(input("\nHow much would you like to deposit: "))
account.deposit(deposit_amount)
print("\n\tAmount deposited")

print(account.to_string())