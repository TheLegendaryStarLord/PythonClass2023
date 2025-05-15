

class Person:
    def __init__(self, name, address, age):
        self.__name = name
        self.__address = address
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def to_string(self):
        return f"Name: {self.__name}, Address: {self.__address}, Age: {self.__age}"