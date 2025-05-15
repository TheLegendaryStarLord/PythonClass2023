#!/usr/bin/env python3
#   Adam Sanchez
#   Cuyamaca College CS-119
#   Lab 3, Exercise 1, Calculate the price for a portait based on differing variables

# Input
Height_In = float(input("Please input your height in inches: "))
Weight_lbs = float(input ("Please input your weight in pounds: "))

# Calculate
meters = Height_In / 39.37;
kilograms = Weight_lbs / 2.2;

BMI = kilograms / meters**2;

#BMI OUTPUT

if BMI <= 18.5:
    print(str(BMI) + ": You are classed at Underweight");
elif BMI >= 18.6 and BMI <= 25:
    print(str(BMI) + ": You are classed at Normal Weight");
elif BMI >= 26 and BMI <= 30:
    print(str(BMI) + ": You are classed at Overweight");
elif BMI >= 31 and BMI <= 35:
    print(str(BMI) + ": You are classed at Obesity (Class 1)");
elif BMI >= 36 and BMI <= 40:
    print(str(BMI) + ": Your are classed at Obesity (Class 2)");
else:
    print(str(BMI) + ": You are classed at Morbid Obesity");
