#!/usr/bin/env python3
#   Adam Sanchez
#   Cuyamaca College CS-119
#   Lab 7, Exercise 2, use classes to determine prices


from Pizza import Pizza

toppings = input("\n\tEnter Toppings: ")
sz = input("\tEnter size (Small, Medium, Large): ")
qty = input("\tEnter quantity: ")

my_pizza = Pizza(toppings, sz, qty)
print("\n\t", my_pizza.to_string() + "\n")