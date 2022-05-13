#Importing tkinter to use for creating a GUI
from tkinter import *
from tkinter.ttk import *

#Dictionary to contain all of the information from the user
details = {'delivery': False, 'name': 'Oliver', 'address': 'No where', 'phone': '0800', 'pizza1':'', 'pizza2':'', 'pizza3':'', 'pizza4':'', 'pizza5':'',}

#set up the tk variables
window = Tk()
window.geometry("700x500")
window.title('Henderson Pizza Place')

leftside = Frame(window, relief="sunken", borderwidth=3)
top = Frame(leftside)
deliveryframe = Frame(leftside)
entryframe = Frame(leftside)
sideframe = LabelFrame(window, text='Your Order:')
pizzaframe = Frame(leftside)
ingredientframe = Frame(leftside)

#set up list variables
labeltexts = ['Would you like delivery or pick up?', 'What name is this order under?', 'Where is this delivered to?', 'What is your Phone number?', 'What preset would you like to use?', 'FILLER1', 'FILLER2', 'FILLER3']
button1texts = ['Delivery', '']
button2texts = ['Pick up', '']
entry_labels = ['Name:', 'Address:', 'Phone number:', '']
pizzas_and_toppings = [['None', 'Classic cheese', 'Pineapple island', 'Multitudinal of meat', 'Mushroom and meats', 'Vegan mix', 'BBQ spice', 'Crunchy chick salad', 'Crunchy chick island'], ['Dragons delight', 'The whole shabang', 'saturday night smoko', 'Vegan majestic composite', "Vegetarian's exspansive collation"], ['grated cheese', 'pineapple', 'ham', 'sliced mushroom', 'olives', 'spinich', 'sliced onion', 'grated carrot', 'grated vegan cheese', 'sliced jalapenos', 'diced carolina reapers', 'crunchy chicken pieces']]

#set up text variables
delvorpick = StringVar()
delvorpick.set('Pick Up')
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
        if details['delivery'] == True:
            delvorpick.set('Delivery')
            grid_widget(label2, 1, 0, 10, 20)
            grid_widget(address_label, 2, 0)
            grid_widget(address_entry, 2, 1)
            grid_widget(label3, 3, 0, 10, 20)
            grid_widget(phone_label, 4, 0)
            grid_widget(phonenumber_entry, 4, 1)
        grid_widget(confirm_button, 5, 0, 10, 10)
        hide_widget(blankspacer)
        grid_widget(side_delivery, y = 10)
    elif part == 2:
        print('second')
        update_details(part)
        labelling1.set(labeltexts[4])
        hide_widget(entryframe)
        grid_widget(sidenamepre, 1)
        grid_widget(side_name, 1, 1)
        if details['delivery'] == True:
            grid_widget(sideaddresspre, 2)
            grid_widget(side_address, 2, 1)
            grid_widget(sidephonepre, 3)
            grid_widget(side_phone, 3, 1)
        grid_widget(pizzaframe)
    elif part == 3:
        print('Third')
        update_details(part)
        hide_widget(pizzaframe)
        grid_widget(ingredientframe)
        part = 1


def delivery_command():
    #so that I can update delivery and not if it is pick up
    global part
    update_details(part)
    update_window()

def update_details(x):
    global details
    if x == 0:
        details['delivery'] = True
    elif x == 1:
        details['name'] = entered.get()
        details['address'] = Addressed.get()
        details['phone'] = Phoned.get()
    elif x == 2:
        print('chaos')

def hide_widget(widget):
    widget.grid_forget()

def grid_widget(widget, Row=0, Column=0, x=10, y=3):
    widget.grid(row=Row, column=Column, padx=x, pady=y, sticky='NSEW')

#Start of set up for visual interactives
grid_widget(leftside, y=10)
grid_widget(top, y=10)
grid_widget(deliveryframe, Row=1, y=10)
sideframe.grid(row=0, column=1, columnspan= 2, padx=10, pady=10, sticky='NSEW')

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

# Creating the parts for the side bar
blankspacer = Label(sideframe, text='')
grid_widget(blankspacer)

side_delivery = Label(sideframe, textvariable=delvorpick)

sidenamepre = Label(sideframe, text='Name: ')
side_name = Label(sideframe, textvariable=entered)

sideaddresspre = Label(sideframe, text='Address: ')
side_address = Label(sideframe, textvariable=Addressed)

sidephonepre = Label(sideframe, text='Phone Number: ')
side_phone = Label(sideframe, textvariable=Phoned)

#pizza preset options - 14 pizzas, 1 blank, 8 reg, 5 gorm

none_button = Button(pizzaframe, text='None').grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky='WE')

Regual_label = Label(pizzaframe, text='Regual pizza').grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky='WE')

cheesepizza = PhotoImage(file="pizza's_pngs\cheesepizza.png")
cheese_button = Button(pizzaframe, text='Classic cheese', image=cheesepizza).grid(row=2, column=0, padx=5, pady=5, sticky='WE')
hawaii_button = Button(pizzaframe, text='Pineapple island').grid(row=2, column=1, padx=5, pady=5, sticky='WE')
meat_button = Button(pizzaframe, text='Multitudinal of meat').grid(row=3, column=0, padx=5, pady=5, sticky='WE')
mushroom_button = Button(pizzaframe, text='Mushroom and meats').grid(row=3, column=1, padx=5, pady=5, sticky='WE')
vegan_button = Button(pizzaframe, text='Vegan mix').grid(row=4, column=0, padx=5, pady=5, sticky='WE')
BBQ_button = Button(pizzaframe, text='BBQ spice').grid(row=4, column=1, padx=5, pady=5, sticky='WE')
chick_button = Button(pizzaframe, text='Crunchy chick salad').grid(row=5, column=0, padx=5, pady=5, sticky='WE')
chick_hawaii_button = Button(pizzaframe, text='Crunchy chick island').grid(row=5, column=1, padx=5, pady=5, sticky='WE')

Gourmet_label = Label(pizzaframe, text='Gourmet Pizzas').grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky='WE')

dragons_button = Button(pizzaframe, text='Dragons delight').grid(row=7, column=0, padx=5, pady=5, sticky='WE')
shabang_button = Button(pizzaframe, text='The whole shabang').grid(row=7, column=1, padx=5, pady=5, sticky='WE')
smoko_button = Button(pizzaframe, text='saturday night smoko').grid(row=8, column=0, padx=5, pady=5, sticky='WE')
vegan_plus_button = Button(pizzaframe, text='Vegan majestic composite').grid(row=8, column=1, padx=5, pady=5, sticky='WE')
vegetarian_button = Button(pizzaframe, text="Vegetarian's exspansive collation").grid(row=9, column=0, columnspan=2, padx=5, pady=5, sticky='WE')

#pizza toppings
cheesecheck = Checkbutton(ingredientframe, text='Grated cheese', onvalue=1, offvalue=0).grid(row=0, column=0)
vegancheck = Checkbutton(ingredientframe, text='Grated vegan cheese', onvalue=1, offvalue=0).grid(row=0, column=1)
pinecheck = Checkbutton(ingredientframe, text='Pineapple', onvalue=1, offvalue=0).grid(row=1, column=0)
hamcheck = Checkbutton(ingredientframe, text='Ham', onvalue=1, offvalue=0).grid(row=1, column=1)
mushcheck = Checkbutton(ingredientframe, text='Sliced mushroom', onvalue=1, offvalue=0).grid(row=2, column=0)
olivecheck = Checkbutton(ingredientframe, text='Olives', onvalue=1, offvalue=0).grid(row=2, column=1)
spinecheck = Checkbutton(ingredientframe, text='Spinich', onvalue=1, offvalue=0).grid(row=3, column=0)
onioncheck = Checkbutton(ingredientframe, text='sliced onion', onvalue=1, offvalue=0).grid(row=3, column=1)
carrotcheck = Checkbutton(ingredientframe, text='Grated carrot', onvalue=1, offvalue=0).grid(row=4, column=0)
jalacheck = Checkbutton(ingredientframe, text='Sliced jalapenos', onvalue=1, offvalue=0).grid(row=4, column=1)
reapercheck = Checkbutton(ingredientframe, text='diced carolina reapers', onvalue=1, offvalue=0).grid(row=5, column=0)
chickcheck = Checkbutton(ingredientframe, text='Crunchy chicken pieces', onvalue=1, offvalue=0).grid(row=5, column=1)

#execute the set up
window.mainloop()
