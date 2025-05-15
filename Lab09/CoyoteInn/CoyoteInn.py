#!/usr/bin/env python3
# Cuyamaca College CS-119
# Adam Sanchez
# Lab 9, exercise 3, Updated Coyotee Inn GUI

from tkinter import *
from tkinter import messagebox

def calc_charges():
    #input
    month = int(txtMonth.get())
    nights = float(txtNights.get())
    
    #process
    if 1 <= month <= 3:
        nightly_rate = 80
    elif 4 <= month <= 6:
        nightly_rate = 90
    elif 7 <= month <= 9:
        nightly_rate = 120
    elif 10 <= month <= 12:
        nightly_rate = 100
    else:
        nightly_rate = 0
        messagebox.showerror('I looked up this error message online', 'Error: invalid month number')
    
    total_charges = nights * nightly_rate
    
    #output
    str_total_charges.set( "{:.2f}".format(total_charges))
    
    
def exit_program():
    # exit(0)
    frm.destroy()
    
frm = Tk()
frm.title("Coyote Inn - Nightly Charges")
frm.geometry('400x200')  # Adjusted form size

# Labels, components, widgets
lblMonth = Label(frm, text="Enter Month (1-12): ", height=1, width=20)
lblMonth.grid(row=0, column=0)
txtMonth = Entry(frm, width=8)
txtMonth.grid(row=0, column=1)

lblNights = Label(frm, text="Enter Number of Nights: ", height=1, width=20)
lblNights.grid(row=1, column=0)
txtNights = Entry(frm, width=8)
txtNights.grid(row=1, column=1)

# Output fields
str_total_charges = StringVar()
lblTextTotal = Label(frm, text="Total Charges: ", height=1, width=15)
lblTextTotal.grid(row=3, column=0)
lblTotal = Label(frm, text="", height=1, width=10, textvariable=str_total_charges)
lblTotal.grid(row=3, column=1)

# Buttons with adjusted columnspan to center them
btnCalc = Button(frm, text="Calculate", command=calc_charges, height=1, width=10)
btnCalc.grid(row=4, column=0, columnspan=2, pady=10)

btnExit = Button(frm, text="Exit", command=exit_program, height=1, width=10)
btnExit.grid(row=5, column=0, columnspan=2)

frm.mainloop()