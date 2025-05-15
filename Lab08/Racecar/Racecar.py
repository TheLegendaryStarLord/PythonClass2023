#!/usr/bin/env python 3
# Cuyamaca College CS-119
# Adam Sanchez
# Lab 8, Exercise 2, Convertible class

from RacecarClass import RacecarClass

make = input("Enter make: ")
model = input("Enter model: ")
vin = input("Enter VIN: ")
color = input("Enter color: ")

horse_power = int(input("Enter the Horse Power: "))

race_car = RacecarClass(vin, make, model, color, horse_power)

print(race_car.to_string())