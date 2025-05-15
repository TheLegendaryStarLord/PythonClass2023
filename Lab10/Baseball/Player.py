#!/usr/bin/env python 3
# Cuyamaca College CS-119
# Adam Sanchez
# From: Lab 8, Exercise 3, player class
# Lab 10, Ex 1: custom Exceptions
# single underscore _var == protected
# double underscore __var == private

from CustomExceptions import InvalidPlayerNumberException

class Player(object):
    def __init__(self, name, number):
        self.__name = name
        self.set_number(number)
        
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
        
    def get_number(self):
        return self.__number
    
    def set_number(self, number):
        MIN_NUMBER = 1
        MAX_NUMBER = 999
        if MIN_NUMBER <= number <= MAX_NUMBER:
            self.__number = number
        else:
            raise InvalidPlayerNumberException
            
    def to_string(self):
        return "({0}) {1}".format(self.get_number(), self.get_name())