#!/usr/bin/env python3
# Adam Sanchez
# Cuyamaca College CS-119
# Lab 1, Exercise 3, Convert Miles to Kilometers

#Variables
MilesPerKm = 0.62
Miles = float(input("Please enter the amount of Miles: "));

#process
KM = Miles / MilesPerKm;

#Display
print(str(Miles) + " Miles is equal to " + str(KM) + "KM");
