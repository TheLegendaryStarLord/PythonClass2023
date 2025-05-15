#!/usr/bin/env python 3
# Cuyamaca College CS-119
# Adam Sanchez
# Lab 8, Exercise 3, Basketball player class

# single underscore _var == protected
# double underscore __var == private

from CustomExceptions import InvalidBattingException
from Player import Player

class BaseballPlayer(Player):
    def __init__(self, name, number, position, batting_avg):
        super().__init__(name, number)
        self.__position = position
        self.set_batting_avg(batting_avg)
        self.__batting_avg = batting_avg

    def get_position(self):
        return self.__position
    
    def set_position(self, position):
        self.__position = position
        
    def get_batting_avg(self):
        return self.__batting_avg
    
    def set_batting_avg(self, batting_avg):
        if batting_avg < 0 or batting_avg > 1.0:
            raise InvalidBattingException("Batting Average must be between 0 - 1.0")
        self.__batting_avg = batting_avg
        
    def to_string(self):
        return super().to_string() \
        + ', Position ' + self.__position \
        + ', Batting Average %0.3f' % self.__batting_avg