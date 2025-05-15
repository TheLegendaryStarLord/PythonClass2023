#!/usr/bin/env python3
#   Adam Sanchez
#   Cuyamaca College CS-119
#   Lab 6, Exercise 2, integer code search method


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
