#!/usr/bin/env python 3
# Cuyamaca College CS-119
# Adam Sanchez
# Lab 10, ex 2 add custom exceptions

from CustomExceptions import InvalidAgeException, InvalidUnitsException, InvalidYearsException
from employee import Employee
from Student import Student

try:
    # Input for an employee
    name = input("Enter name: ")
    address = input("Enter address: ")
    age = int(input("Enter age: "))
    skills = input("Enter job skills: ")
    years_worked = int(input("Enter years worked: "))
    major = input("Enter student major: ")
    units_completed = int(input("Enter units completed: "))

    # Create instances of Employee and Student
    employee = Employee(name, address, age, skills, years_worked)
    student = Student(name, address, age, major, units_completed)

    # Display the information
    print("Employee Info:")
    print(employee.to_string())

    print("\nStudent Info:")
    print(student.to_string())

except InvalidAgeException as A_E:
    print("Invalid Age Exception: ", A_E)
except InvalidUnitsException as U_E:
    print("Invalid Units Exception: ", U_E)
except InvalidYearsException as Y_E:
    print("Invalid Years Exception: ", Y_E)
except Exception as E:
    print("Generic Exception: ", E)