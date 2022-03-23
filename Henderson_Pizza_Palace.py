#Importing tkinter to use for creating a GUI
from tkinter import *

#Dictionary to contain all of the information from the user
order = {'delivery': False, 'name': '', 'address': '', 'phone': ''}

#set up the variables
window = Tk()
top = Frame(window)
buttons = Frame(window)

#set up for the window
top.pack()
buttons.pack()

label1 = Label(top, text = "Do you want your order delivered or will you pick it up?")
label1.pack()

deliverbutton = Button(buttons, text = 'Delivery')
deliverbutton.pack()

pickupbutton = Button(buttons, text = 'Pick up')
pickupbutton.pack()

#execute the set up
window.mainloop()

