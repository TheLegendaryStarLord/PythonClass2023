#!/usr/bin/env python3
#   Adam Sanchez
#   Cuyamaca College CS-119
#   Lab 7, Exercise 1, class exercise

class Magazine:
    
    def __init__(self, subscriber_name, magazine_title, months_remaining):
        self.__subscriber_name = subscriber_name
        self.__magazine_title = magazine_title
        self.__months_remaining = months_remaining
        

    def get_subscriber_name(self):
        return self.__subscriber_name
    

    def set_subscriber_name(self, subscriber_name):
        self.__subscriber_name = subscriber_name
    
    def get_magazine_title(self):
        return self.__magazine_title
    
    def set_magazine_title(self, magazine_title):
        self.__magazine_title = magazine_title
        
    def get_months_remaining(self):
        return self.__months_remaining
    
    def set_months_remaining(self, months_remaining):
        self.__months_remaining = months_remaining
        
    def to_string(self):
        return f"Subscriber name: {self.__subscriber_name} " \
                f"Title : {self.__magazine_title}: {self.__months_remaining} months remaining"