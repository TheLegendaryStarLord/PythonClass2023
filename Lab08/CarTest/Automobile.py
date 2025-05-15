#!/usr/bin/env python 3
# Cuyamaca College CS-119
# Adam Sanchez
# Lab 8, Exercise 1, Automobile class

# single underscore _var == protected
# double underscore __var == private

class Automobile:
    def __init__(self, vin, make, model, color):
        self.__vin = vin
        self.__make = make
        self.__model = model
        self.__color = color
        #getters
    def get_vin(self):
        return self.__vin
    
    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model
    
    def get_color(self):
        return self.__color
    #setters
    def set_vin(self, vin):
        self.__vin = vin
        
    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model
    
    def set_color(self, color):
        self.__color = color
        
    def to_string(self):
        return "\nVIN: " + self.__vin + " \nmake: " \
        + self.__make + " \nmodel: " + self.__model \
        + " \ncolor: " + self.__color