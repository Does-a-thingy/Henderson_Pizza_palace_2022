#Importing tkinter to use for creating a GUI
from tkinter import *
from tkinter.ttk import *

#Dictionary to contain all of the information from the user
details = {'delivery': False, 'name': 'Oliver', 'address': 'No where', 'phone': '0800'}

#set up the tk variables
window = Tk()
window.title('Henderson Pizza Place')
top = Frame(window)
deliveryframe = Frame(window)
entryframe = Frame(window)

#set up list variables
labeltexts = ['Would you like delivery or pick up?', 'What name is this order under?', 'Where is this delivered to?', 'What is your Phone number?', '']
button1texts = ['Delivery', '']
button2texts = ['Pick up', '']
entry_labels = ['Name:', 'Address:', 'Phone number:', '']

#set up text variables
labelling1 = StringVar()
labelling1.set(labeltexts[0])
buttoning1 = StringVar()
buttoning1.set(button1texts[0])
buttoning2 = StringVar()
buttoning2.set(button2texts[0])
detailentry_labels = StringVar()
detailentry_labels.set(entry_labels[0])

#set up argument variables
x = 0
part = 0

# set up the functions
def update_window():
    global x, part
    part += 1
    x += 1
    labelling1.set(labeltexts[part])
    if x == 1:
        print('first')
        hide_widget(deliveryframe)
        grid_widget(entryframe, 1, 0, 10, 10)
        grid_widget(detail_label, 0, 0)
        grid_widget(name_entry, 0, 1)
        grid_widget(confirm_button, 1, 0, 10, 10)
    elif x == 2:
        print('second')
        hide_widget(name_entry)
        update_details(x)
        #checking if delivery is true then procedding accordingly
        if details['delivery'] == True:
            detailentry_labels.set(entry_labels[1])
            grid_widget(address_entry, 0, 1)
            detailentry_labels.set('address')
    elif x == 3:
        print('third')

def delivery_command():
    # so that I can update delivery and not if it is pick up
    global x
    update_window()
    update_details(x)

def update_details(x):
    global details, name
    if x == 1:
        details['delivery'] = True
        print(details['delivery'])
    elif x == 2:
        details['name'] = name
        print(details['name'])
    elif x == 3:
        print('yeet')

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
name = DoubleVar()
name.set('Name')

detail_label = Label(entryframe, textvariable=detailentry_labels)

name_entry = Entry(entryframe, textvariable=name)

confirm_button = Button(entryframe, text='Confirm', command=update_window)

#set up for address gathering
address = DoubleVar()
address.set('address')

address_entry = Entry(entryframe, textvariable=address)

#execute the set up
window.mainloop()
