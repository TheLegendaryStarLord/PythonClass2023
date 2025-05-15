#!/usr/bin/env python 3
# Cuyamaca College CS-119
# Adam Sanchez
# Lab 8, Exercise 2, Convertible class

from Automobile import Automobile

class RacecarClass(Automobile):
    def __init__(self, vin, make, model, color, horse_power):
#override the Automobile constructor so call the inherited constructor
        super().__init__(vin, make, model, color)
        self._horse_power = horse_power
        
        #setter and getter
    def get_horse_power(self):
        return self._horse_power
    
    def set_horse_power(self, horse_power):
        self._horse_power = horse_power
        
        #string
    def to_string(self):
        return super().to_string() \
            + " \nhorse power: " + str(self._horse_power)