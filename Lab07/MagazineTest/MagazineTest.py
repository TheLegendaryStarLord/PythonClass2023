#!/usr/bin/env python3
#   Adam Sanchez
#   Cuyamaca College CS-119
#   Lab 7, Exercise 1, class exercise

from Magazine import Magazine

subscriber_name = input("Enter subscriber name: ")
magazine_title = input("Enter Magazine title: ")
months_remaining = int(input("Enter months remaining: "))

my_magazine = Magazine(subscriber_name, magazine_title, months_remaining)

print(my_magazine.to_string())