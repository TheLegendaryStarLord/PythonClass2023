#!/usr/bin/env python 3
# Cuyamaca College CS-119
# Adam Sanchez
# Lab 8, Exercise 3, Basketball player class

# single underscore _var == protected
# double underscore __var == private

from Player import Player

class BaseballPlayer(Player):
    def __init__(self, name, number, position, batting_avg):
        super().__init__(name, number)
        self.__position = position
        self.__batting_avg = batting_avg

    def get_position(self):
        return self.__position
    
    def set_postion(self, position):
        self.__position = position
        
    def get_battingAvg(self):
        return self.__batting_avg
    
    def set_battingAvg(self, batting_avg):
        self.__batting_avg = batting_avg
        
    def to_string(self):
        return super().to_string() \
        + ' Position ' + self.__position \
        + ' Batting Average %0.3f' % self.__batting_avg