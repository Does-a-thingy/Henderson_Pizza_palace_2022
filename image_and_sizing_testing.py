from tkinter import *
from tkinter.ttk import *

window = Tk()
window.geometry("700x500")
window.title('Image and image sizing testing')

pizzaframe = Frame(window).grid(row=0, column=0, padx=10, pady=10)

cheesepizza1 = PhotoImage(file="pizza's_pngs\cheesepizza.png").subsample(5,5)
cheese_button1 = Button(pizzaframe, image=cheesepizza1).grid(row=0, column=0, padx=5, sticky='WE')
cheese_label1 = Label(pizzaframe, text='5, 5').grid(row=1, column=0, sticky='WE')

cheesepizza2 = PhotoImage(file="pizza's_pngs\cheesepizza.png").subsample(10,10)
cheese_button2 = Button(pizzaframe, image=cheesepizza2).grid(row=0, column=1, padx=5, pady=5, sticky='WE')
cheese_label2 = Label(pizzaframe, text='10, 10').grid(row=1, column=1, sticky='WE')

cheesepizza3 = PhotoImage(file="pizza's_pngs\cheesepizza.png").subsample(15,5)
cheese_button3 = Button(pizzaframe, image=cheesepizza2).grid(row=2, column=0, padx=5, pady=5, sticky='NS')
cheese_label3 = Label(pizzaframe, text='15, 5').grid(row=3, column=0, sticky='WE')

cheesepizza4 = PhotoImage(file="pizza's_pngs\cheesepizza.png").subsample(5,15)
cheese_button4 = Button(pizzaframe, image=cheesepizza4).grid(row=2, column=1, padx=5, pady=5, sticky='NS')
cheese_label4 = Label(pizzaframe, text='5, 15').grid(row=3, column=1, sticky='WE')

cheesepizza5 = PhotoImage(file="pizza's_pngs\cheesepizza.png").subsample(5,15)
cheese_button5 = Button(pizzaframe, image=cheesepizza5).grid(row=4, column=0, padx=5, pady=5, sticky='WE')
cheese_label5 = Label(pizzaframe, text='5, 15').grid(row=5, column=0, sticky='WE')

cheesepizza6 = PhotoImage(file="pizza's_pngs\cheesepizza.png").subsample(5,18)
cheese_button6 = Button(pizzaframe, image=cheesepizza6).grid(row=4, column=1, padx=5, pady=5, sticky='NSEW')
cheese_label6 = Label(pizzaframe, text='5, 18').grid(row=5, column=1, sticky='NSEW')
