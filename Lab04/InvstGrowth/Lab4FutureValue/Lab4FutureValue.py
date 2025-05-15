#!/usr/bin/env python3
#   Adam Sanchez
#   Cuyamaca College CS-119
#   Lab 4, Exercise 1, factorial

# Variable
Monthly_amt = 0
years = 0
AnnIntRate = 0.0
MonthlyIntRate = 0.0
fv = 0.0
months = 0
month_num = 1

# msg python format
msg = "Month: {0:3d} FV: ${1:.2f} Interest: ${2:.2f}"
interest = 0.0
totalInt = 0.0

#input
Monthly_amt = float(input("Enter monthly amount: "))
AnnIntRate = float(input("Enter Annual Interest Rate: "))
years = int(input("Enter number of Years: "))

#process
MonthlyIntRate = AnnIntRate / 100 / 12
months = years * 12

#loop
while month_num <= months:
    '''
    I wasnt sure what equation to use since the monthly 100 isnt apart of the interest (probably)
    theres properly one that simpler but this seems to work so im not going to question it for now
    '''
    interest = ((fv + Monthly_amt) * (1 + MonthlyIntRate)) - (fv + Monthly_amt)

    fv = (fv + Monthly_amt) * (1 + MonthlyIntRate)

    totalInt += interest
    print(msg.format(month_num, fv, interest))
    month_num += 1;

print("\n\nTotal interest: ${0:.2f}".format(totalInt))