from tkinter import *
from tkinter.ttk import *

window = Tk()
window.geometry("700x500")
window.title('Image and image sizing testing')

pizzaframe = Frame(window).grid(row=0, column=0, padx=10, pady=10)

cheesepizza1 = PhotoImage(file="pizza's_pngs\cheesepizza.png").subsample(5,5)
cheese_button1 = Button(pizzaframe, text='5, 5', image=cheesepizza1, compound=TOP).grid(row=0, column=0, padx=5, sticky='WE')

cheesepizza2 = PhotoImage(file="pizza's_pngs\cheesepizza.png").subsample(10,10)
cheese_button2 = Button(pizzaframe, text='10, 10', image=cheesepizza2, compound=TOP).grid(row=0, column=1, padx=5, pady=5, sticky='WE')

cheesepizza3 = PhotoImage(file="pizza's_pngs\cheesepizza.png").subsample(15,5)
cheese_button3 = Button(pizzaframe, text='15, 5', image=cheesepizza2, compound=TOP).grid(row=2, column=0, padx=5, pady=5, sticky='WE')

cheesepizza4 = PhotoImage(file="pizza's_pngs\cheesepizza.png").subsample(5,15)
cheese_button4 = Button(pizzaframe, text='5, 15, NS', image=cheesepizza4, compound=TOP).grid(row=2, column=1, padx=5, pady=5, sticky='NS')

cheesepizza5 = PhotoImage(file="pizza's_pngs\cheesepizza.png").subsample(5,15)
cheese_button5 = Button(pizzaframe, text='5, 15', image=cheesepizza5, compound=TOP).grid(row=4, column=0, padx=5, pady=5, sticky='WE')

cheesepizza6 = PhotoImage(file="pizza's_pngs\cheesepizza.png").subsample(5,18)
cheese_button6 = Button(pizzaframe, text='5, 18', image=cheesepizza6, compound=TOP).grid(row=4, column=1, padx=5, pady=5, sticky='NSEW')
