#Importing tkinter to use for creating a GUI
from tkinter import *
from tkinter.ttk import *

#Dictionary to contain all of the information from the user
order = {'delivery': False, 'name': '', 'address': '', 'phone': ''}

#set up the tk variables
window = Tk()
window.title('Henderson Pizza Place')
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
buttoning1 = StringVar()
buttoning1.set(button1texts[0])
buttoning2 = StringVar()
buttoning2.set(button2texts[0])

#set up argument variables
x = 0
part = 0

# set up the functions
def update_window():
    global x, part
    part += 1
    x += 1
    if x == 1:
        print('first')
        labelling1.set(labeltexts[part])
        hide_widget(deliveryframe)
        grid_widget(nameframe, 1, 0, 10, 10)
        grid_widget(name_label, 0, 0)
        grid_widget(name_entry, 0, 1)
        grid_widget(confirm_button, 1, 0, 10, 10)
    elif x == 2:
        print('second')
        hide_widget(nameframe)

    elif x == 3:
        print('third')

def update_deliver():
    order['delivery'] = True
    update_window()

def address_update():
    print('b')

def hide_widget(widget):
    widget.grid_forget()

def grid_widget(widget, Row=0, Column=0, x=10, y=3):
    widget.grid(row=Row, column=Column, padx=x, pady=y, sticky='NSEW')
#set up for the window
grid_widget(top, y=10)
grid_widget(deliveryframe, 1, 0, 10, 10)

label1 = Label(top, textvariable = labelling1)
label1.grid(row=0, column=0, padx=10, pady=3)

#delivery or pick up buttons
deliverbutton = Button(deliveryframe, textvariable=buttoning1, command=update_deliver)
deliverbutton.grid(row=0, column=0, padx=10, pady=3, columnspan=2, sticky='WE')

pickupbutton = Button(deliveryframe, textvariable=buttoning2, command=update_window)
pickupbutton.grid(row=1, column=0, padx=10, pady=3, columnspan=2, sticky='WE')

#getting name entry and submit button
name = DoubleVar()
name.set('')

name_label = Label(nameframe, text='Name:')

name_entry = Entry(nameframe, textvariable=name)

confirm_button = Button(nameframe, text='Confirm', command=update_window)
#execute the set up
window.mainloop()
