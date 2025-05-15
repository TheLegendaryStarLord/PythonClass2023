#!/usr/bin/env python3
#   Adam Sanchez
#   Cuyamaca College CS-119
#   Lab 4, Exercise 1, loop demo definite loop with fixed number of iterations

# Variables Constants
number = 0;
exponent = 0;

# input
number = int(input("Enter a number: "))
exponent = int(input("Enter the Exponent: "))
i = 0
result = 1

#loop
while i < exponent:
    result = result * number
    i+=1

print("the result is " + str(result))