#!/usr/bin/env python3
#   Adam Sanchez
#   Cuyamaca College CS-119
#   Lab 7, Exercise 4, Burger class for restuarant


class Burger:
    def __init__(self, customer_name, order_number, burger_type, quantity_ordered):
        self.customer_name = customer_name
        self.order_number = order_number
        self.burger_type = burger_type
        self.quantity_ordered = quantity_ordered
        self.price = self.calculate_price()

    def get_customer_name(self):
        return self.customer_name

    def set_customer_name(self, customer_name):
        self.customer_name = customer_name

    def get_order_number(self):
        return self.order_number

    def set_order_number(self, order_number):
        self.order_number = order_number

    def get_burger_type(self):
        return self.burger_type

    def set_burger_type(self, burger_type):
        self.burger_type = burger_type

    def get_quantity_ordered(self):
        return self.quantity_ordered

    def set_quantity_ordered(self, quantity_ordered):
        self.quantity_ordered = quantity_ordered
        self.price = self.calculate_price()

    def calculate_price(self):
        if self.burger_type.lower() == "regular":
            return 1.75 * self.quantity_ordered
        elif self.burger_type.lower() == "cheese":
            return 2.00 * self.quantity_ordered
        elif self.burger_type.lower() == "double meat":
            return 3.50 * self.quantity_ordered
        elif self.burger_type.lower() == "double meat, bacon & cheddar":
            return 4.50 * self.quantity_ordered
        else:
            return 0.0 
    def to_string(self):
        return f"Customer Name: {self.customer_name}\nOrder Number: {self.order_number}\nBurger Type: {self.burger_type}\nQuantity Ordered: {self.quantity_ordered}\nTotal Price: ${self.price:.2f}"





