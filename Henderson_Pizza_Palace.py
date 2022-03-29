#Importing tkinter to use for creating a GUI
from tkinter import *

#Dictionary to contain all of the information from the user
order = {'delivery': False, 'name': '', 'address': '', 'phone': ''}

#set up the tk variables
window = Tk()
top = Frame(window)
buttons = Frame(window)

# set up the functions
def update_window():
    print('working')
    
def update_deliver():
    order['delivery'] = True
    update_window()

#set up for the window
top.grid(row=0, column=0, padx=10, pady=10)
buttons.grid(row=1, column=0, padx=10, pady=10)

label1 = Label(top, text = "Do you want your order delivered or will you pick it up?")
label1.grid(row=0, column=0, padx=10, pady=3)

deliverbutton = Button(buttons, text = 'Delivery', command=update_deliver)
deliverbutton.grid(row=0, column=0, padx=10, pady=3, columnspan=2, sticky='WE')

pickupbutton = Button(buttons, text = 'Pick up', command=update_window)
pickupbutton.grid(row=1, column=0, padx=10, pady=3, columnspan=2, sticky='WE')

#execute the set up
window.mainloop()

