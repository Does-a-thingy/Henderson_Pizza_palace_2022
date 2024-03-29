#Importing tkinter to use for creating a GUI
from tkinter import *
from tkinter.ttk import *

#Dictionary to contain all of the information from the user
details = {'delivery': False, 'name': 'Oliver', 'address': 'No where', 'phone': '0800', 'pizza1':'', 'pizza2':'', 'pizza3':'', 'pizza4':'', 'pizza5':''}

#set up the tk variables
window = Tk()
window.geometry('1000x1000')
window.state('zoomed')
window.title('Henderson Pizza Place')

leftside = Frame(window, relief="sunken", borderwidth=3)
top = Frame(leftside)
deliveryframe = Frame(leftside)
entryframe = Frame(leftside)
sideframe = LabelFrame(window, text='Your Order:')
pizzaframe = Frame(leftside)
ingredientframe = Frame(leftside)
totalframe = Frame(window)

#set up list variables
labeltexts = ['Would you like delivery or pick up?', 'What name is this order under?', 'Where is this delivered to?', 'What is your Phone number?', 'What preset would you like to use?', 'ingredients']
button1texts = ['Delivery', '']
button2texts = ['Pick up', '']
entry_labels = ['Name:', 'Address:', 'Phone number:', '']

pizzas = [['None', 'Classic cheese', 'Pineapple island', 'Multitudinal of meat', 'Mushroom and meats', 'Vegan mix', 'BBQ spice', 'Crunchy chick salad', 'Crunchy chick island'], ['Dragons delight', 'The whole shabang', 'saturday night smoko', 'Vegan majestic composite', "Vegetarian's exspansive collation"]]

toppings = ['grated cheese', 'pineapple', 'ham', 'sliced mushroom', 'olives', 'spinich', 'sliced onion', 'grated carrot', 'grated vegan cheese', 'sliced jalapenos', 'diced carolina reapers', 'crunchy chicken pieces', 'pepperoni', 'mini meat balls', 'BBQ sauce', 'Pizza sauce']

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

#set up python variables
part = 0
loopcheck = True
pizzaname = ''
loopcount = 0
grandtot = 0
total = 0
totloop = 1

# set up the functions
def update_window():
    global part, loopcheck, loopcount
    part += 1
    labelling1.set(labeltexts[part])
    if loopcount < 5:
        if part == 1:
            print('first')
            hide_widget(deliveryframe)
            grid_widget(entryframe, 1, 0, 10, 10)
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
            if loopcheck == True:
                hide_widget(entryframe)
                grid_widget(sidenamepre, 1)
                grid_widget(side_name, 1, 1)
                if details['delivery'] == True:
                    grid_widget(sideaddresspre, 2)
                    grid_widget(side_address, 2, 1)
                    grid_widget(sidephonepre, 3)
                    grid_widget(side_phone, 3, 1)
                grid_widget(pizzaframe)
            elif loopcheck == False:
                hide_widget(ingredientframe)
                grid_widget(pizzaframe)
                if loopcount == 1:
                    grid_widget(side_order1, 4)
                elif loopcount == 2:
                    grid_widget(side_order2, 5)
                elif loopcount == 3:
                    grid_widget(side_order3, 6)
                elif loopcount == 4:
                    grid_widget(side_order4, 7)
                elif loopcount == 5:
                    grid_widget(side_order5, 8)
                    hide_widget(sideframe)
                    grid_widget(totalframe, y=10)
        elif part == 3:
            print('Third')
            update_details(part)
            hide_widget(pizzaframe)
            grid_widget(ingredientframe)
            part = 1
            loopcheck = False
            if loopcount < 5:
                loopcount += 1

def delivery_command():
    #so that I can update delivery and not if it is pick up
    global part
    update_details(part)
    update_window()

def update_details(x):
    global details
    if x == 0:
        #runs after the delivery or pick up
        details['delivery'] = True
    elif x == 1:
        #runs for the entry boxes
        details['name'] = entered.get()
        details['address'] = Addressed.get()
        details['phone'] = Phoned.get()
    elif x == 2:
        #runs for the pizza
        print('chaos')

def hide_widget(widget):
    widget.grid_forget()

def grid_widget(widget, Row=0, Column=0, clmspn=1, x=10, y=3, stic='NSEW'):
    widget.grid(row=Row, column=Column, columnspan=clmspn, padx=x, pady=y, sticky=stic)

def finish_command():
    hide_widget(leftside)
    grid_widget(totalframe, y=10)

def cancel_command():
    window.destroy()

def running_totaling():
    global loopcount, piz1_total, piz2_total, piz3_total, piz4_total, piz5_total, total, totloop
    onpizza = ''
    if loopcount >= 1 and totloop == 1:
        piz1_total = total
        totloop += 1
    elif loopcount >= 2 and totloop == 2:
        piz2_total = total
        totloop += 1
    elif loopcount >= 3 and totloop == 3:
        piz3_total = total
        totloop += 1
    elif loopcount >= 4 and totloop == 4:
        piz4_total = total
        totloop += 1
    elif loopcount == 5 and totloop == 5:
        piz5_total = total

def final_totaling():
    global grandtot, pizzaname, piz1_total, piz2_total, piz3_total, piz4_total, piz5_total
    grandtot = piz1_total + piz2_total + piz3_total + piz4_total + piz5_total

#Pizza Commands to transition to ingredients with presets.
def cheesepizza_command():
    global cheese, pizzaname, total
    total = 7
    cheese = 1
    pizzaname = 'Classic cheese'
    update_window()

def hawaiipizza_command():
    global cheese, pine, hame, pizzaname, total
    total = 7
    cheese = 1
    pine = 1
    hame = 1
    pizzaname = "Pineapple island"
    update_window()

def meatpizza_command():
    global hame, mball, pepper, cheese, pizzaname, total
    total = 7
    cheese = 1
    hame = 1
    mball = 1
    pepper = 1
    pizzaname = "Multitudinal of meat"
    update_window()

def mushpizza_command():
    global mush, mball, pepper, cheese, pizzaname, total
    total = 7
    cheese = 1
    mush = 1
    mball = 1
    pepper = 1
    pizzaname = "Mushroom and meat"
    update_window()

def vegan_command():
    global vegan, mush, charrot, spine, pizzaname, total
    total = 7
    vegan = 1
    mush =1
    charrot = 1
    spine = 1
    pizzaname = "Vegan mix"
    update_window()

def BBQ_command():
    global cheese, hame, pepper, sauce, jala, pizzaname, total
    total = 7
    cheese = 1
    hame = 1
    pepper = 1
    jala = 1
    bsaucerad.invoke()
    pizzaname = 'spicy BBQ'
    update_window()

def chicksal_command():
    global cheese, chick, charrot, spine, pizzaname, total
    total = 7
    cheese = 1
    chick = 1
    charrot = 1
    spine = 1
    pizzaname = 'Crunchy chick salad'
    update_window()

def chickpine_command():
    global cheese, chick, pine, pizzaname, total
    total = 7
    cheese = 1
    chick = 1
    pine = 1
    pizzaname = 'Crunchy chick island'
    update_window()

def drag_command():
    global cheese, jala, pepper, sauce, oliver, reap, pizzaname, total
    total = 8.5
    cheese = 1
    jala = 1
    pepper = 1
    oliver = 1
    reap = 1
    bsaucerad.invoke()
    pizzaname = 'Dragons delight'
    update_window()

def shab_command():
    global cheese, hame, pepper, oliver, spine, pine, mush, mball, chick, onion, charrot, pizzaname, total
    total = 8.5
    cheese = 1
    hame = 1
    pepper = 1
    oliver = 1
    spine = 1
    pine = 1
    mush = 1
    mball = 1
    chick = 1
    onion = 1
    charrot = 1
    pizzaname = 'The whole Shabang'
    update_window()

def veganmaj_command():
    global vegan, oliver, spine, pine, mush, charrot, onion, jala, pizzaname, total
    total = 8.5
    vegan = 1
    oliver = 1
    spine = 1
    pine = 1
    mush = 1
    charrot = 1
    onion = 1
    jala = 1
    pizzaname = 'Vegan majestic composite'
    update_window()

def smoko_command():
    global cheese, hame, oliver, charrot, jala, spine, pine, sauce, mball, pepper, pizzaname, total
    total = 8.5
    cheese = 1
    hame = 1
    oliver = 1
    charrot = 1
    jala = 1
    spine = 1
    pine = 1
    mball = 1
    pepper = 1
    bsaucerad.invoke()
    pizzaname = 'saturday night smoko'
    update_window()

def veggie_command():
    global cheese, mush, charrot, pine, oliver, spine, reap, onion, pizzaname, total
    total = 8.5
    cheese = 1
    mush = 1
    charrot = 1
    pine = 1
    oliver = 1
    spine = 1
    reap = 1
    onion = 1
    pizzaname = "Vegetarian's exspansive collation"
    update_window()

#Start of set up for visual interactives
grid_widget(leftside, y=10)
grid_widget(top, y=10)
grid_widget(deliveryframe, Row=1, y=10)
sideframe.grid(row=0, column=1, columnspan= 2, padx=10, pady=10, sticky='NSEW')

# cancel and finsh buttons
finish_button = Button(sideframe, text='Finish', command=finish_command)
grid_widget(finish_button, 9)

cancel_button = Button(sideframe, text='Cancel', command=cancel_command)
grid_widget(cancel_button, 10)

#main label
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
grid_widget(name_label, 0, 0)
name_entry = Entry(entryframe, textvariable=entered)
grid_widget(name_entry, 0, 1)
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
noneimage = PhotoImage(file="pizza's_pngs\Blank.png").subsample(8,8)
none_button = Button(pizzaframe, text='None', image=noneimage, compound=TOP, command=update_window)
grid_widget(none_button, Column=1)

Regual_label = Label(pizzaframe, text='Regual pizza')
grid_widget(Regual_label, Row=1, clmspn=3, x=5, y=5, stic='WE')

cheesepizza = PhotoImage(file="pizza's_pngs\cheesepizza.png").subsample(8,8)
cheese_button = Button(pizzaframe, text='Classic cheese', image=cheesepizza, compound=TOP, command=cheesepizza_command)
grid_widget(cheese_button, Row=2, x=5, y=5)

hawaiiimage = PhotoImage(file="pizza's_pngs\pineapple_pizza.png").subsample(11,11)
hawaii_button = Button(pizzaframe, text='Pineapple island', image=hawaiiimage, compound=TOP, command=hawaiipizza_command)
grid_widget(hawaii_button, Row=2, Column=1, x=5, y=5)

meatimage = PhotoImage(file="pizza's_pngs\multi_meat_pizza.png").subsample(4,4)
meat_button = Button(pizzaframe, text='Multitudinal of meat', image=meatimage, compound=TOP, command=meatpizza_command)
grid_widget(meat_button, Row=2, Column=2, x=5, y=5)

mushyimage = PhotoImage(file="pizza's_pngs\mushroom_meat_pizza.png").subsample(8,8)
mushroom_button = Button(pizzaframe, text='Mushroom and meats', image=mushyimage, compound=TOP, command=mushpizza_command)
grid_widget(mushroom_button, Row=2, Column=3, x=5, y=5)

veganimage = PhotoImage(file="pizza's_pngs\minor_vegan_pizza.png").subsample(5,5)
vegan_button = Button(pizzaframe, text='Vegan mix', image=veganimage, compound=TOP, command=vegan_command)
grid_widget(vegan_button, Row=3, x=5, y=5)

BBQimage = PhotoImage(file="pizza's_pngs\spicy_BBQ_pizza.png").subsample(8,8)
BBQ_button = Button(pizzaframe, text='BBQ spice', image=BBQimage, compound=TOP, command=BBQ_command)
grid_widget(BBQ_button, Row=3, Column=1, x=5, y=5)

chickimage = PhotoImage(file="pizza's_pngs\crunchy_chick.png").subsample(4,4)
chick_button = Button(pizzaframe, text='Crunchy chick salad', image=chickimage, compound=TOP, command=chicksal_command)
grid_widget(chick_button, Row=3, Column=2, x=5, y=5)

chickpineimage = PhotoImage(file="pizza's_pngs\crunch_chick_pineapple.png").subsample(4,4)
chick_hawaii_button = Button(pizzaframe, text='Crunchy chick island', image=chickpineimage, compound=TOP, command=chickpine_command)
grid_widget(chick_hawaii_button, Row=3, Column=3, x=5, y=5)

Gourmet_label = Label(pizzaframe, text='Gourmet Pizzas')
grid_widget(Gourmet_label, Row=5, clmspn=3, x=5, y=5)

dragonimage = PhotoImage(file="pizza's_pngs\Dragon_pizza.png").subsample(3,3)
dragons_button = Button(pizzaframe, text='Dragons delight', image=dragonimage, compound=TOP, command=drag_command)
grid_widget(dragons_button, Row=6, x=5, y=5)

shabangimage = PhotoImage(file="pizza's_pngs\whole_shabang.png").subsample(7,7)
shabang_button = Button(pizzaframe, text='The whole shabang', image=shabangimage, compound=TOP, command=shab_command)
grid_widget(shabang_button, Row=6, Column=1, x=5, y=5)

Veganimage = PhotoImage(file="pizza's_pngs\Vegan_major_pizza.png").subsample(8,8)
vegan_plus_button = Button(pizzaframe, text='Vegan majestic composite', image=Veganimage, compound=TOP, command=veganmaj_command)
grid_widget(vegan_plus_button, Row=6, Column=2, x=5, y=5)

smokoimage = PhotoImage(file="pizza's_pngs\smoko_pizza.png").subsample(12,12)
smoko_button = Button(pizzaframe, text='saturday night smoko', image=smokoimage, compound=TOP, command=smoko_command)
grid_widget(smoko_button, Row=7, x=5, y=5)

veggieimage = PhotoImage(file="pizza's_pngs\Veggie_pizza.png").subsample(4,4)
vegetarian_button = Button(pizzaframe, text="Vegetarian's exspansive collation", image=veggieimage, compound=TOP, command=veggie_command)
grid_widget(vegetarian_button, Row=7, Column=1, x=5, y=5)

#pizza toppings - Sauce and ingredients
# Sauce
sauce_label = Label(ingredientframe, text='Sauce: ')
grid_widget(sauce_label, x=3, y=3)

sauce = IntVar()
psaucerad = Radiobutton(ingredientframe, text='Pizza Sauce', variable=sauce, value=0)
grid_widget(psaucerad, Row=1, x=3, y=3)
bsaucerad = Radiobutton(ingredientframe, text='BBQ Sauce', variable=sauce, value=1)
grid_widget(bsaucerad, Row=1, Column=1, x=3, y=3)

# seperator
gredientslab = Label(ingredientframe, text='ingredients: ')
grid_widget(gredientslab, Row=2, clmspn=2, x=5, y=5)

# ingredients
cheese = IntVar()
cheesecheck = Checkbutton(ingredientframe, text='Grated cheese', variable=cheese, onvalue=1, offvalue=0).grid(row=3, padx=3, pady=3)

vegan = IntVar()
vegancheck = Checkbutton(ingredientframe, text='Grated vegan cheese', variable=vegan, onvalue=1, offvalue=0).grid(row=3, column=1, padx=3, pady=3)

pine = IntVar()
pinecheck = Checkbutton(ingredientframe, text='Pineapple', variable=pine, onvalue=1, offvalue=0).grid(row=4, padx=3, pady=3)

hame = IntVar()
hamcheck = Checkbutton(ingredientframe, text='Ham', variable=hame, onvalue=1, offvalue=0).grid(row=4, column=1, padx=3, pady=3)

mush = IntVar()
mushcheck = Checkbutton(ingredientframe, text='Sliced mushroom', variable=mush, onvalue=1, offvalue=0).grid(row=5, padx=3, pady=3)

oliver = IntVar()
olivecheck = Checkbutton(ingredientframe, text='Olives', variable=oliver, onvalue=1, offvalue=0).grid(row=5, column=1, padx=3, pady=3)

spine = IntVar()
spinecheck = Checkbutton(ingredientframe, text='Spinich', variable=spine, onvalue=1, offvalue=0).grid(row=6, padx=3, pady=3)

onion = IntVar()
onioncheck = Checkbutton(ingredientframe, text='Sliced onion', variable=onion, onvalue=1, offvalue=0).grid(row=6, column=1, padx=3, pady=3)

charrot = IntVar()
carrotcheck = Checkbutton(ingredientframe, text='Grated carrot', variable=charrot, onvalue=1, offvalue=0).grid(row=7, column=0, padx=3, pady=3)

jala = IntVar()
jalacheck = Checkbutton(ingredientframe, text='Sliced jalapenos', variable=jala, onvalue=1, offvalue=0).grid(row=7, column=1, padx=3, pady=3)

reap = IntVar()
reapercheck = Checkbutton(ingredientframe, text='Diced carolina reapers', variable=reap, onvalue=1, offvalue=0).grid(row=8, column=0, padx=3, pady=3)

chick = IntVar()
chickcheck = Checkbutton(ingredientframe, text='Crunchy chicken pieces', variable=chick, onvalue=1, offvalue=0).grid(row=8, column=1, padx=3, pady=3)

pepper = IntVar()
peppercheck = Checkbutton(ingredientframe, text='Pepperoni', variable=pepper, onvalue=1, offvalue=0).grid(row=9, column=0, padx=3, pady=3)

mball = IntVar()
mballcheck = Checkbutton(ingredientframe, text='Mini Meat Ball', variable=mball, onvalue=1, offvalue=0).grid(row=9, column=1, padx=3, pady=3)

ingredient_confirm = Button(ingredientframe, text='Confirm', command=update_window)
grid_widget(ingredient_confirm, Row=10, clmspn=2, x=5, y=5)

# Order side label
order1 = StringVar()
side_order1 = Label(sideframe, textvariable=order1)

order2 = StringVar()
side_order2 = Label(sideframe, textvariable=order2)

order3 = StringVar()
side_order3 = Label(sideframe, textvariable=order3)

order4 = StringVar()
side_order4 = Label(sideframe, textvariable=order4)

order5 = StringVar()
side_order5 = Label(sideframe, textvariable=order5)

# Total for each pizza + extras + grand total
piz1_total = IntVar()
piz2_total = IntVar()
piz3_total = IntVar()
piz4_total = IntVar()
piz5_total = IntVar()

piz1_lab = Label(totalframe, textvariable=order1)
grid_widget(piz1_lab, 1, y=10)

piz2_lab = Label(totalframe, textvariable=order2)
grid_widget(piz2_lab, 1, y=10)

piz3_lab = Label(totalframe, textvariable=order3)
grid_widget(piz3_lab, 1, y=10)

piz4_lab = Label(totalframe, textvariable=order4)
grid_widget(piz4_lab, 1, y=10)

piz5_lab = Label(totalframe, textvariable=order5)
grid_widget(piz5_lab, 1, y=10)

#execute the set up
window.mainloop()
