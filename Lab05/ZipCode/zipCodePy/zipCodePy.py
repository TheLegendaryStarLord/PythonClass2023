#!/usr/bin/env python3
#   Adam Sanchez
#   Cuyamaca College CS-119
#   Lab 5, Exercise 1, Uses loops to check lists for zip codes

#parallel lists of zip codes
zips = [93927, 33904, 30030, 44024];
cities = ["Greenfield", "Cape Coral", "Decatur", "Chardon"]
states = ["Ca", "Fl", "Ga", "Oh"]

#zip codes
zipCode = 00000;
city = "Unknown";
state = "UN";
found = False; #error1 accidentally put false in quotations
i = 0;
listLength = len(zips); #used to get list length, remember this!!!!

#input 
zipCode = int(input("Please enter a zip code: "))

#Linear search
while i < listLength and not found:
    
    if zipCode == zips[i]:#checks if true
        
        city = cities[i]
        state = states[i]
        found = True;
    i = i + 1; #increment
#End while

#output
print("zips: " + str(zipCode) + "   City: " + city + "  State: " + state);