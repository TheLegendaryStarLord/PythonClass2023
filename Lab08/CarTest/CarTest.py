#!/usr/bin/env python 3
# Cuyamaca College CS-119
# Adam Sanchez
# Lab 8, Exercise 1, Convertible class test fixture

from Convertable import Convertable

print("Convertable: ")
make = input("Enter make: ")
model = input("Enter model: ")
vin = input("Enter VIN: ")
color = input("Enter color: ")
top_up_name = input("Enter is top up? (Yes/No): ")

if top_up_name.upper() == "YES":
    is_top_up = True
else:
    is_top_up = False
    
my_car = Convertable(vin, make, model, color, is_top_up)

print(my_car.to_string())