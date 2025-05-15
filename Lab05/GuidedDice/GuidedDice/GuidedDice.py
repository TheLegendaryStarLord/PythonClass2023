#!/usr/bin/env python3
#   Adam Sanchez
#   Cuyamaca College CS-119
#   Lab 5, Exercise 2, using loops and arrays to make dice game

import random

#variables
maxRolls = 5
maxDiceValue = 6

#roll Types
rollTypes = ["Junk", "Pair", "3 of a kind", "4 of a kind", "5 of a kind"]

#list initialization for dice rolls and tally
pDice = [0,0,0,0,0]
cDice = [0,0,0,0,0]
# 6 in size for values 1-6
pTally = [0,0,0,0,0,0]
cTally = [0,0,0,0,0,0]

#roll dice
i = 0
while i < maxRolls:
    rollVal = random.randint(1, maxDiceValue)
    pDice[i] = rollVal
    rollVal = random.randint(1, maxDiceValue)
    cDice[i] = rollVal
    i += 1

#print values#

#Display player roll
i = 0
print("The Player Rolled: ", end=" ")
while i < maxRolls:
    print(pDice[i], end=" ")
    i += 1

i = 0
print("\nThe Computer Rolled", end=" ")
while i < maxRolls:
    print(cDice[i], end=" ")
    i += 1

#tally list to determine rollTypes
i = 0
while i < maxRolls:
    pTally [ pDice[i] - 1] += 1
    cTally [ cDice[i] - 1] += 1
    i += 1

#find out how many 2's 3's 4's and determine roll types
pMax = pTally[0]
cMax = cTally[0]

i = 1
while i < maxDiceValue:
    if pMax < pTally[i]:
        pMax = pTally[i]
        #end if
    if cMax < cTally[i]:
        cMax = cTally[i]
        #end if
    i += 1
#end loop

#output
print("\nPlayer Rolled: " + rollTypes[pMax - 1])
print("Computer Rolled: " + rollTypes[cMax - 1])

#Determine winner
if pMax > cMax:
    print("Player Wins!")
elif cMax > pMax:
    print("Computer Wins!")
else:
    print("Tie!")