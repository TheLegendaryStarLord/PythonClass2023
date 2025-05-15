#!/usr/bin/env python3
# Cuyamaca College CS-119
# Adam Sanchez
# Lab 9, exercise 1, Miles per Gallon GUI

from tkinter import *

def calc_mileage():
    #input
    miles = float(txtMiles.get())
    gallons = float(txtGallons.get())
    cost_per_gal = float(txtCostPerGal.get())
    
    #process
    mpg = miles/gallons
    total_fuel_cost = gallons * cost_per_gal
    cost_per_mile = total_fuel_cost / miles
    
    #output
    str_mpg.set( "{:.2f}".format(mpg))
    str_cpm.set( "${:.2f}".format(cost_per_mile))
    str_tot_fuel_cost.set( "${:.2f}".format(total_fuel_cost))
    
def exit_program():
    # exit(0)
    frm.destroy()
    
frm = Tk()
frm.title("Find your MPG")
frm.geometry('450x200')#form size

#labels, components, widgets
lblMiles = Label(frm, text="Miles Driven: ", height = 1, width = 12)
lblMiles.grid(row=0, column = 0)
#Entry is single line
txtMiles = Entry(frm, width=8)
txtMiles.grid(row=0, column=1)

lblGallons = Label(frm, text="Gallons Purchased: ", height=1, width=15)
lblGallons.grid(row=0, column=2)
txtGallons = Entry(frm, width = 8)
txtGallons.grid(row=0, column=3)

lblCostPerGal = Label(frm, text="Cost per Gallon: ", height=1, width=12)
lblCostPerGal.grid(row=1, column=0)
txtCostPerGal = Entry(frm, width=8)
txtCostPerGal.grid(row=1, column=1)

#output fields
str_mpg = StringVar()
lblTextMPG = Label(frm, text="Your MPG is: ", height=1, width=10)
lblTextMPG.grid(row=2, column=0)
lblMPG = Label(frm, text="", height=1, width=10, textvariable=str_mpg)
lblMPG.grid(row=2, column=1)

str_tot_fuel_cost = StringVar()
lblTextTotFuel = Label(frm, text="Total Fuel Cost: ", height=1, width=12)
lblTextTotFuel.grid(row=3, column=0)
lbltotFuel = Label(frm, text="", height=1, width=10, textvariable=str_tot_fuel_cost)
lbltotFuel.grid(row=3, column=1)

str_cpm = StringVar()
lblTextCPM = Label(frm, text="COst per Mile: ", height = 1, width=12)
lblCPM = Label(frm, text="", height=1, width=10, textvariable=str_cpm)
lblCPM.grid(row=4, column=1)

# in the command = we bind the button press event handler to the control
btnCalc = Button(frm, text="Calculate", command=calc_mileage, height=1, width=10)
btnCalc.grid(row=6, column=0)

btnExit = Button(frm, text="Exit", command=exit_program, height=1, width=10)
btnExit.grid(row=7, column=0)

frm.mainloop()