#!/usr/bin/env python3
#   Adam Sanchez
#   Cuyamaca College CS-119
#   Lab 6, Exercise 2, use prices based on tour codes and entered number of people


import MethodCoyote

# Parallel arrays for tour codes, destinations, and cost per person
tour_codes = [1001, 1002, 1003, 1004, 1005, 1006]
destinations = ["Destination1", "Destination2", "Destination3", "Destination4", "Destination5", "Destination6"]
costPerPersons = [50.00, 60.00, 70.00, 80.00, 90.00, 100.00]

def main():
    
    i = MethodCoyote.find_int(tour_codes, int(input("Enter a tour code number: ")))
    numOfPersons = int(input("Enter the Number of people: "))
    
    if i != -1:
        
        destination = destinations[i]
        costPerPerson = costPerPersons[i]
        totalPrice = costPerPerson * numOfPersons

        # Display
        print("Destination: " + str(destination))
        print("Cost per person: " + str(costPerPerson))
        print("Number of persons: " + str(numOfPersons))
        print("Total price: " + str(totalPrice) )
    else:
        # Invalid tour code
        print("NOT FOUND")
        print("Cost per person: $0.00")

if __name__ == "__main__":
    main()