#!/usr/bin/env python 3
# Cuyamaca College CS-119
# Adam Sanchez
# Lab 12, Array/list sorting

from array import array
from sort_integers import sort_integers

numInput = input("Enter you list of numbers seperated by spaces: ")
numList = list(map(int, numInput.split()))


sort_integers(numList)

sortedArray = array('i', numList)

print(" ".join(map(str, sortedArray)))