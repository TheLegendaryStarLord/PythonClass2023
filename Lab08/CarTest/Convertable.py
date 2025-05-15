#!/usr/bin/env python 3
# Cuyamaca College CS-119
# Adam Sanchez
# Lab 8, Exercise 1, Convertible class

from Automobile import Automobile

# a single underscore _var makes it protected
# a double underscore __var makes it private

class Convertable(Automobile):
#custom constructor
    def __init__(self, vin, make, model, color, is_top_up):
#override the Automobile constructor so call the inherited constructor
        super().__init__(vin, make, model, color)
#add any extra code needed for the convertible constructor
        self._is_top_up = is_top_up
        
#getter and setter
    def get_is_top_up(self):
        return self._is_top_up
    
    def set_is_top_up(self, is_top_up):
        _is_top_up = is_top_up
        
#public instance method to format the status of top up/down
    def fmt_top_status(self):
        status = "No" #No by default
        if self._is_top_up == True:
            status = "Yes"
        return status
    
#instance method
    def to_string(self):
        return super().to_string() \
        +"\nis top up?: " + self.fmt_top_status()