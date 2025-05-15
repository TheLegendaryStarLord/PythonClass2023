#!/usr/bin/env python3
#   Adam Sanchez
#   Cuyamaca College CS-119
#   Lab 6, Exercise 1, methods exercise

def get_float_val(prompt):
    is_num = False
    str_val = input(prompt)
    while is_num == False:
        try:
            value = float(str_val)
            is_num = True
        except:
            print(str_val + " is not a float!")
            str_val = input(prompt)
    #end while

    return value
#end get_float_val()

def get_int_val(prompt):
    is_num = False
    str_val = input(prompt)
    while is_num == False:
        try:
            value = int(str_val)
            is_num = True
        except:
            print(str_val + " is not an Int!")
            str_val = input(prompt)

    return value
#end get_int_val()

def is_float(value):
    try:
        num = float(value)
        return True
    except:
        return False

def is_integer(value):
    try:
        num = int(value)
        return True
    except:
        return False

def find_string(the_list, find_val):
    list_len = len(the_list)
    found = False
    i = 0
    idx = -1
    while i < list_len and found == False:
        if find_val.upper() == the_list[i].upper():
            idx = i
            found = True
        i += 1

    return idx

def find_int(int_list, val_find):
    list_len = len(int_list)
    found = False
    i = 0
    idx = -1
    while i < list_len and not found:
        if int_list[i] == val_find:
            idx = i
            found = True
        i += 1
    return idx
