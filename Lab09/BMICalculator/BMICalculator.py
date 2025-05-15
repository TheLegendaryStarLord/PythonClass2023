#!/usr/bin/env python3
# Cuyamaca College CS-119
# Adam Sanchez
# Lab 9, exercise 2, BMI calculator GUI

from tkinter import *

def calc_mileage():
    #input
    kilograms = float(txtKilo.get())
    meters = float(txtmeters.get())
    
    #process
    bmi = kilograms / meters**2
    
    #output
    str_bmi.set( "{:.2f}".format(bmi))
    
    
def exit_program():
    # exit(0)
    frm.destroy()
    
frm = Tk()
frm.title("Find your BMI")
frm.geometry('450x250')#form size

#labels, components, widgets
lblKilo = Label(frm, text="What is your weight in Kilograms: ", height = 1, width = 29)
lblKilo.grid(row=0, column = 0)
#Entry is single line
txtKilo = Entry(frm, width=8)
txtKilo.grid(row=0, column=1)

lblmeters = Label(frm, text="What is your height in Meters: ", height=1, width=25)
lblmeters.grid(row=1, column=0)
txtmeters = Entry(frm, width = 8)
txtmeters.grid(row=1, column=1)

#output fields
str_bmi = StringVar()
lblTextBMI = Label(frm, text="Your BMI is: ", height=1, width=10)
lblTextBMI.grid(row=3, column=0)
lblBMI = Label(frm, text="", height=1, width=10, textvariable=str_bmi)
lblBMI.grid(row=3, column=1)

# in the command = we bind the button press event handler to the control
btnCalc = Button(frm, text="Calculate", command=calc_mileage, height=1, width=10)
btnCalc.grid(row=7, column=0, columnspan=2, pady=10)

btnExit = Button(frm, text="Exit", command=exit_program, height=1, width=10)
btnExit.grid(row=8, column=0, columnspan=2)

frm.mainloop()