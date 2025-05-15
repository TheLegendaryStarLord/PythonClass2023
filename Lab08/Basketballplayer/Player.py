#!/usr/bin/env python 3
# Cuyamaca College CS-119
# Adam Sanchez
# Lab 8, Exercise 4, player class

# single underscore _var == protected
# double underscore __var == private

class Player:
    def __init__(self, name, number):
        self._name = name
        self.set_number(number)
        
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name
        
    def get_number(self):
        return self._number
    
    def set_number(self, number):
        MIN_NUMBER = 1
        MAX_NUMBER = 999
        if number >= MIN_NUMBER and number <= MAX_NUMBER:
            self._number = number
        else:
            self._number = MIN_NUMBER
            
    def to_string(self):
        return "({0}) {1}".format(self._number, self._name)