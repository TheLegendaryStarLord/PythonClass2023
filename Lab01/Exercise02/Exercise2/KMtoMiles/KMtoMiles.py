#!/usr/bin/env python3
# Adam Sanchez
# Cuyamaca College CS-119
# Lab 1, Exercise 2, Convert Kilometers to Miles

#Variables
MilesPerKM = 0.62;
km = float(input("Enter kilometers: "));

#Process
Miles = MilesPerKM * km;

#Output
print(str(km) +  " KM is equal to " + str(Miles) + " Miles");
