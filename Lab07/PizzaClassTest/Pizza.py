#!/usr/bin/env python3
#   Adam Sanchez
#   Cuyamaca College CS-119
#   Lab 7, Exercise 2, use classes to determine prices

import Methods as m

class Pizza:
    __sizes = ["Small", "Medium", "Large"]
    __prices = [8.00, 10.00, 12.00]
    
    def __init__(self, toppings, size, quantity):
        self.__price = 0.0
        self.__toppings = toppings
        self.__quantity = quantity
        self.set_size(size)
        
    def get_toppings(self):
        return self.__toppings
    
    def set_toppings(self, toppings):
        self.__toppings = toppings
        
    def get_size(self):
        return self.__size
    
    def set_size(self, size):
        idx = m.find_string(self.__sizes,size)
        
        if idx >= 0:
            self.__size = size
            self.__price = self.__prices[idx]
            
        else:
            self.__size = Pizza.__sizes[0]
            self.__price = Pizza.__prices[0]
            
    def get_quantity(self):
        return self.__quantity
    
    def set_quantity(self, quantity):
        if quantity < 0:
            quantity = 0
        self.__quantity = quantity
    
    def calculate_price(self):
        return self.__price * float(self.__quantity)
    
    def to_string(self):
        ext_price = self.calculate_price()
        return "qty: " + str(self.__quantity) + " sz: " + self.__size + \
        " with "+ self.__toppings + " Total: ${:.2f}".format(ext_price)