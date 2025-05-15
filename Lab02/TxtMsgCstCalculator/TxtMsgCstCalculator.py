#!/usr/bin/env python3
#   Adam Sanchez
#   Cuyamaca College CS-119
#   Lab 2, Exercise 1, Calculate the cost of messages for the month

#variable declaration
MsgCost = 0.25;
tax = 0.09;
NmbrOfTxts = 0;

#input
NmberOfTxts = int(input("Please Input the number of Texts you have sent this month: "));

#equation process
CostPerMsg = (NmberOfTxts * MsgCost);
TotalSale = (CostPerMsg * tax) + CostPerMsg;

#Display
print("The cost before tax is: " + str(CostPerMsg));
print("The total cost of messages for this month is: " + str(TotalSale));