#!/usr/bin/env python3
#   Adam Sanchez
#   Cuyamaca College CS-119
#   Lab 4, Exercise 1, factorial

import random

# variables
MaxFlips = 20
maxVal = 2
heads = 0.0
tails = 0.0
pctTails = 0.0 #percent heads
pctHeads = 0.0 #percent tails
i = 0
flip = 0

for i in range(1, MaxFlips + 1 , 1):
    flip = random.randint(0,1)
    if flip == 0:
        print("Flip #" + str(i) + ': Heads')
        heads+=1
    elif flip == 1:
        print("Flip #" + str(i) + ': Tails')
        tails+=1

print("Total heads: {0}".format(heads))
print("Total tails: {0}".format(tails))

pctHeads = (heads / MaxFlips) * 100.0
pctTails = (tails / MaxFlips) * 100.0

print("Pct heads: %{0:.1f}".format(pctHeads))
print("Pct tails: %{0:.1f}".format(pctTails))