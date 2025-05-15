#!/usr/bin/env python3
#   Adam Sanchez
#   Cuyamaca College CS-119
#   Lab 7, Exercise 4, Burger main for restuarant

from BurgerClass import Burger

customer_name = input("Enter Customer Name: ")
order_number = input("Enter Order Number: ")
burger_type = input("Enter Burger Type (Regular, Cheese, Double meat, Double meat, bacon & cheddar): ")
quantity_ordered = int(input("Enter Quantity Ordered: "))

burger = Burger(customer_name, order_number, burger_type, quantity_ordered)

print(burger.to_string())
