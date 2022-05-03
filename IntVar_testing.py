from tkinter import *

win = Tk()
win.geometry("500x500")

num1 = IntVar()
num2 = IntVar()
total_number = IntVar()
total_list = ['']

showthing = StringVar()

Label(win, textvariable = showthing).pack()

def show():
    global total_list, total_number
    showthing.set('total_list {}, total_number {}'.format(total_list.get(), total_number.get()))

num1.set(4)
num2.set(7)

total_number.set(num1+num2)
