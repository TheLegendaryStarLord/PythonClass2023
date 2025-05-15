#!/usr/bin/env python 3
# Cuyamaca College CS-119
# Adam Sanchez
# Lab 10, ex 2 add custom exceptions

from CustomExceptions import InvalidUnitsException
from Person import Person

class Student(Person):
    def __init__(self, name, address, age, major, units_completed):
        super().__init__(name, address, age)
        self.__major = major
        self.set_units_completed(units_completed)

    def get_major(self):
        return self.__major

    def set_major(self, major):
        self.__major = major

    def get_units_completed(self):
        return self.__units_completed

    def set_units_completed(self, units_completed):
        if units_completed < 0 or units_completed > 200:
            raise InvalidUnitsException("Units must be between 0 and 200")
        else:
            self.__units_completed = units_completed

    def to_string(self):
        person_info = super().to_string()
        return f"{person_info}, Major: {self.__major}, Units Completed: {self.__units_completed}"



