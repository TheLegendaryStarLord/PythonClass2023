#!/usr/bin/env python3
#   Adam Sanchez
#   Cuyamaca College CS-119
#   Lab 5, Exercise 3, use an array list of zip codes to calculate shipping costs

#zip codes, prices, locations
zips = [92020, 91901, 92040, 91976, 92071];
cities = ["El Cajon", "Alpine", "Lakeside", "Spring Valley", "Santee"]
expressPrice =  [5.00 , 10.00, 7.00, 6.00, 7.00]
groundPrice = [3.00, 5.00, 4.00, 3.00, 4.00]

#variable initialization
zipCode = 00000;
city = "Unknown";
price = 0.00;
found = False; #error1 accidentally put false in quotations
i = 0;
listLength = len(zips); #used to get list length, remember this!!!!
shipChoice = "Undefined";

#input
zipCode = int(input("Please enter the zip code: "))

while i < listLength and not found:
    if zipCode == zips[i]:  # checks if true
        city = cities[i]
        found = True
    i = i + 1  # increment

if not found: # Check if zip code was not found
    print("Zip code not found")
else:
    shipChoice = input("Please enter \"Express\" or \"Ground\" for your choice of shipping: ").lower()

    i = 0 #index reset, new search

    if shipChoice == "express":
        price = expressPrice[i]
    elif shipChoice == "ground":
        price = groundPrice[i]
    else:
        print("Shipping method invalid")
        

print("Zip: " + str(zipCode) + "   City: " + city + "  Shipping method: " + str(shipChoice) + "  Price: " + str(price));