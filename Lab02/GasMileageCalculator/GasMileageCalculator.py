#!/usr/bin/env python3
#   Adam Sanchez
#   Cuyamaca College CS-119
#   Lab 2, Exercise 2, Calculate the gas mileage

#Variable User Input
gallons = float(input("Please input the number of Gallons: "));
milesDriven = float(input("Please input the miles the car has driven: "));
costPerGallon = float(input("Please input the cost each gallon costs: "));

#Equation Process
mpg = milesDriven / gallons
totalFuelCost = gallons * costPerGallon;
costPerMile = totalFuelCost / milesDriven;

#Display
print("The MPG of the car is : " + str(mpg) + "\n");
print("The total fuel cost is : " + str(totalFuelCost) + "\n");
print("The cost per mile is : " + str(costPerMile) + "\n");