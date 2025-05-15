#!/usr/bin/env python 3
# Cuyamaca College CS-119
# Adam Sanchez
# Lab 8, Exercise 3, basketball test

# single underscore _var == protected
# double underscore __var == private

from BasketballPlayerclass import BasketballPlayerclass

name = input("Enter name: ")
number = int(input("Enter number: "))
position = input("Enter position: ")
freeThrowPer = float(input("Enter free throw percentage: "))

my_player = BasketballPlayerclass(name, number, position, freeThrowPer)

print(my_player.to_string())
