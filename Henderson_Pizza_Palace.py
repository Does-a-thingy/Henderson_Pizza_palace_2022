#Importing tkinter to use for creating a GUI
from tkinter import *
from tkinter.ttk import *

#Dictionary to contain all of the information from the user
details = {'delivery': False, 'name': 'Oliver', 'address': 'No where', 'phone': '0800', 'pizza1':'', 'pizza2':'', 'pizza3':'', 'pizza4':'', 'pizza5':'',}

#set up the tk variables
window = Tk()
window.title('Henderson Pizza Place')
top = Frame(window)
deliveryframe = Frame(window)
entryframe = Frame(window)

#set up list variables
labeltexts = ['Would you like delivery or pick up?', 'What name is this order under?', 'Where is this delivered to?', 'What is your Phone number?', 'What pizza would you like', 'FILLER2', 'FILLER3', 'FILLER4', 'FILLER5']
button1texts = ['Delivery', '']
button2texts = ['Pick up', '']
entry_labels = ['Name:', 'Address:', 'Phone number:', '']

#set up text variables
labelling1 = StringVar()
labelling1.set(labeltexts[0])
labelling2 = StringVar()
labelling2.set(labeltexts[2])
labelling3 = StringVar()
labelling3.set(labeltexts[3])
buttoning1 = StringVar()
buttoning1.set(button1texts[0])
buttoning2 = StringVar()
buttoning2.set(button2texts[0])
detailentry_labels = StringVar()
detailentry_labels.set(entry_labels[0])
address_labels = StringVar()
address_labels.set(entry_labels[1])
phone_labels = StringVar()
phone_labels.set(entry_labels[2])

#set up argument variables
part = 0

# set up the functions
def update_window():
    global part
    part += 1
    labelling1.set(labeltexts[part])
    if part == 1:
        print('first')
        hide_widget(deliveryframe)
        grid_widget(entryframe, 1, 0, 10, 10)
        grid_widget(name_label, 0, 0)
        grid_widget(name_entry, 0, 1)
        grid_widget(label2, 1, 0, 10, 20)
        grid_widget(address_label, 2, 0)
        grid_widget(address_entry, 2, 1)
        grid_widget(label3, 3, 0, 10, 20)
        grid_widget(phone_label, 4, 0)
        grid_widget(phonenumber_entry, 4, 1)
        grid_widget(confirm_button, 5, 0, 10, 10)

    elif part == 2:
        update_details(part)
        part = 4
        labelling1.set(labeltexts[part])
        hide_widget(entryframe)


def delivery_command():
    # so that I can update delivery and not if it is pick up
    global part
    update_window()
    update_details(part)

def update_details(x):
    global details, entered
    if x == 1:
        details['delivery'] = True
    elif x == 2:
        details['name'] = entered.get()
        details['address'] = Addressed.get()
        details['phone'] = Phoned.get()

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
deliverbutton = Button(deliveryframe, textvariable=buttoning1, command=delivery_command)
deliverbutton.grid(row=0, column=0, padx=10, pady=3, columnspan=2, sticky='WE')

pickupbutton = Button(deliveryframe, textvariable=buttoning2, command=update_window)
pickupbutton.grid(row=1, column=0, padx=10, pady=3, columnspan=2, sticky='WE')

#setting up the name entry and submit button
entered = StringVar()
entered.set('')

name_label = Label(entryframe, textvariable=detailentry_labels)
name_entry = Entry(entryframe, textvariable=entered)

#set up for address gathering
label2 = Label(entryframe, textvariable=labelling2)

address_label = Label(entryframe, textvariable=address_labels)
Addressed = StringVar()
Addressed.set('')
address_entry = Entry(entryframe, textvariable=Addressed)

#set up for phone number gathering
label3 = Label(entryframe, textvariable=labelling3)

phone_label = Label(entryframe, textvariable=phone_labels)
Phoned = StringVar()
Phoned.set('')
phonenumber_entry = Entry(entryframe, textvariable=Phoned)

#Create confirm button
confirm_button = Button(entryframe, text='Confirm', command=update_window)

#execute the set up
window.mainloop()
