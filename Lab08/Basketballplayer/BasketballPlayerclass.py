#!/usr/bin/env python 3
# Cuyamaca College CS-119
# Adam Sanchez
# Lab 8, Exercise 4, Basketball player class

# single underscore _var == protected
# double underscore __var == private

from Player import Player

class BasketballPlayerclass(Player):
    def __init__(self, name, number, position, free_throw_percentage):
        super().__init__(name, number)
        self.__position = position
        self.__free_throw_percentage = free_throw_percentage

    def get_position(self):
        return self.__position
    
    def set_postion(self, position):
        self.__position = position
        
    def get_freeThrowPercentage(self):
        return self.__free_throw_percentage
    
    def set_freeThrowPercentage(self, free_throw_percentage):
        self.__free_throw_percentage = free_throw_percentage
        
    def to_string(self):
        return super().to_string() \
        + ' Position: ' + self.__position \
        + ' free throw percentage: %0.3f ' % self.__free_throw_percentage