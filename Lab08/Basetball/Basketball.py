#!/usr/bin/env python 3
# Cuyamaca College CS-119
# Adam Sanchez
# Lab 8, Exercise 3, basetball test

# single underscore _var == protected
# double underscore __var == private

from BaseballPlayer import BaseballPlayer

name = input("Enter name: ")
number = int(input("Enter number: "))
position = input("Enter position: ")
average = float(input("Enter batting average: "))

my_player = BaseballPlayer(name, number, position, average)

print(my_player.to_string())