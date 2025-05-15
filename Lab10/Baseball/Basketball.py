#!/usr/bin/env python 3
# Cuyamaca College CS-119
# Adam Sanchez
# From: Lab 8, Exercise 3, baseball test
# Lab 10, ex 1 add custom exceptions

from BaseballPlayer import BaseballPlayer
from CustomExceptions import InvalidBattingException, InvalidPlayerNumberException

try:
    name = input("Enter name: ")
    number = int(input("Enter number: ")) # range 0 - 999
    position = input("Enter position: ") 
    average = float(input("Enter batting average: ")) # range 0 - 1.0

    my_player = BaseballPlayer(name, number, position, average)

    print(my_player.to_string())
    
except InvalidPlayerNumberException as e:
    print("Invalid player number: ", e)
    
except InvalidBattingException as eb:
    print("Invalid Batting Score: ", eb)
    
except Exception as ex:
    print("Generic Exception: ", ex)