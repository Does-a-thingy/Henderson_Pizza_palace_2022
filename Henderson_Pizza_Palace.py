#Importing tkinter to use for creating a GUI
from tkinter import *

#Dictionary to contain all of the information from the user
order = {'delivery': False, 'name': '', 'address': '', 'phone': ''}

#set up the tk variables
window = Tk()
top = Frame(window)
deliveryframe = Frame(window)
nameframe = Frame(window)

#set up list variables
labeltexts = ['Would you like delivery or pick up?', 'What name is this order under?', 'Where is this delivered to?']
button1texts = ['Delivery', '']
button2texts = ['Pick up', '']

#set up text variables
labelling1 = StringVar()
labelling1.set(labeltexts[0])

#set up counting variables
x = 1
part = 0

# set up the functions
def update_window():
    global x, part
    if x == 1:
        print('first')
        x += 1
        part += 1
        labelling1.set(labeltexts[part])
    elif x == 2:
        print('second')

def update_deliver():
    order['delivery'] = True
    update_window()

def address_update():
    

#set up for the window
top.grid(row=0, column=0, padx=10, pady=10)
buttons.grid(row=1, column=0, padx=10, pady=10, sticky='NSEW')
nameframe.grid(row=2, column=0, padx=10, pady=10, sticky='NSEW')

label1 = Label(top, textvariable = labelling1)
label1.grid(row=0, column=0, padx=10, pady=3)

#delivery or pick up buttons
deliverbutton = Button(deliveryframe, textvariable=button1texts, command=update_deliver)
deliverbutton.grid(row=0, column=0, padx=10, pady=3, columnspan=2, sticky='WE')

pickupbutton = Button(deliveryframe, textvariable=button2texts, command=update_window)
pickupbutton.grid(row=1, column=0, padx=10, pady=3, columnspan=2, sticky='WE')

#getting name entry and submit button
name = DoubleVar()
name.set('')

name_label = Label(nameframe, text='Name:')
name_lavel.grid(row=0)

#execute the set up
window.mainloop()

