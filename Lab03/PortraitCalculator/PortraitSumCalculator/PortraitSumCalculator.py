#!/usr/bin/env python3
#   Adam Sanchez
#   Cuyamaca College CS-119
#   Lab 3, Exercise 1, Calculate the price for a portait based on differing variables


# locale importing
import locale
locale.setlocale(locale.LC_ALL, "en-us")

#Variable Declaration
LastName = "";
NumberOfSubjects = 0;
DayOfWeek = 0;
BasePrice = 0;

SURCHARGE_PCT = 1.2;
SUNDAY = 1;
SATURDAY = 7;


#Input
LastName = str(input("Please Enter Your Last Name: "));
NumberOfSubjects = int(input("Please enter the number of people in your portrait: "));
DayOfWeek = int(input("Please enter the number for day of the week, (Sun = 1, Mon = 2, Tue = 3) "));

# baseprice process
if NumberOfSubjects == 1:
    BasePrice =  100;
elif NumberOfSubjects == 2:
    BasePrice =  130;
elif NumberOfSubjects == 3:
    BasePrice = 150;
elif NumberOfSubjects == 4:
    BasePrice = 165;
elif NumberOfSubjects == 5:
    BasePrice = 175;
elif NumberOfSubjects == 6:
    BasePrice = 180;
else:
   BasePrice = 185;


#Surcharge decision

# Thankfully this works too
'''
if DayOfWeek == 7:
    BasePrice = BasePrice * SURCHARGE_PCT;
elif DayOfWeek == 1:
    BasePrice = BasePrice * SURCHARGE_PCT;
'''
 

# I had no idea you could do it like this \/
if DayOfWeek == SATURDAY or DayOfWeek == SUNDAY:
    BasePrice = BasePrice * SURCHARGE_PCT

#output
print("Last Name: " + LastName)
print("Total price: " + locale.currency(BasePrice, grouping = True));