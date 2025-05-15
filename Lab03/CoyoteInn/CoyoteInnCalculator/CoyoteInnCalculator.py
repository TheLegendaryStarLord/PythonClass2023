#!/usr/bin/env python3
#   Adam Sanchez
#   Cuyamaca College CS-119
#   Lab 3, Exercise 1, Calculate the price for a portait based on differing variables

#Import for currency
import locale
locale.setlocale(locale.LC_ALL, "en-us")

#variable declaration
PricePerNight = 0.0

#user input
Month = int(input("Please input the month number: "));

# Valid number check
if Month < 1 or Month > 12:
    print("Invalid number please restart the program");
    quit

# Price tree based on month
if Month >= 1 and Month <= 3:
    PricePerNight = 80;
elif Month >= 4 and Month <= 6:
    PricePerNight = 90;
elif Month >= 7 and Month <= 9:
    PricePerNight = 120;
elif Month >= 10 and Month <= 12:
    PricePerNight = 100;

#display price
print("Price: " + locale.currency(PricePerNight, grouping = True))