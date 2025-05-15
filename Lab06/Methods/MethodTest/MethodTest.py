#!/usr/bin/env python3
#   Adam Sanchez
#   Cuyamaca College CS-119
#   Lab 6, Exercise 1, methods exercise

import Methods as m

#definning a main() method
def main():
    float_val = m.get_float_val("Enter a floating point number: ")
    print("Float value " + str(float_val) + " was entered")

    int_val = m.get_int_val("Enter an Integer number: ")
    print("Integer value " + str(int_val) + " was entered: ")

    str_val = input("Enter a value: ")
    result = m.is_float(str_val)
    if result == True:
        print(str_val + " is a float.")
    else:
        print(str_val + " is not a float")

    #Find String test
    my_list = ["goat", "ZEBRA", "HorsE", "foX", "dog", "Cat"]
    value = input("Enter a value to find: ")

    idx = m.find_string(my_list, value)

    if idx >= 0:
        print("Found " + value + " at index " + str(idx))
    else:
        print(value + " Not Found!")

    # end of String test

    #Find int test
    my_list = [1, 3, 5, 7, 9, 11]
    val_find = int(input("What int should I search: "))
    indx = m.find_int(my_list, val_find)

    if indx != -1:
        print("The value " + str(val_find) + " was found at index " + str(indx) + ".")
    else:
        print("The value " + str(val_find) + " was not found in the list.")

#main moduel execute main()
if __name__ == "__main__":
    main()

