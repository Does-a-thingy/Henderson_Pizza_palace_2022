from tkinter import *

win = Tk()
win.geometry("500x500")

num1 = IntVar()
num2 = IntVar()
total_number = IntVar()
total_list = [17, 23, 12]

showthing = StringVar()

Label(win, textvariable = showthing).pack()

def show():
    global total_list, total_number
    total_number.set(total_number.get() + num2.get())
    showthing.set(total_number.get())

num1.set(4)
num2.set(7)

total_number.set(num1.get() + num2.get())

showthing.set(total_number.get())

Button(win, text='show', command=show).pack()

win.mainloop()
