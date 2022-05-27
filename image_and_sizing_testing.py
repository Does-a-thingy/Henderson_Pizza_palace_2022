from tkinter import *
from tkinter.ttk import *

window = Tk()
window.geometry("700x500")
window.title('Image and image sizing testing')

pizzaframe = Frame(window).grid(row=0, column=0, padx=10, pady=10)

cheesepizza1 = PhotoImage(file="pizza's_pngs\cheesepizza.png").subsample(5,5)
cheese_button = Button(pizzaframe, text='5 , 5', image=cheesepizza1).grid(row=0, column=0, padx=5, pady=5, sticky='WE')

cheesepizza2 = PhotoImage(file="pizza's_pngs\cheesepizza.png").subsample(10,10)
cheese_button = Button(pizzaframe, text='10 , 10', image=cheesepizza2).grid(row=0, column=1, padx=5, pady=5, sticky='WE')

cheesepizza3 = PhotoImage(file="pizza's_pngs\cheesepizza.png").subsample(15,8)
cheese_button = Button(pizzaframe, text='15 , 8', image=cheesepizza2).grid(row=1, column=0, padx=5, pady=5, sticky='WE')

cheesepizza4 = PhotoImage(file="pizza's_pngs\cheesepizza.png").subsample(12,14)
cheese_button = Button(pizzaframe, text='12 , 14', image=cheesepizza4).grid(row=1, column=1, padx=5, pady=5, sticky='WE')
