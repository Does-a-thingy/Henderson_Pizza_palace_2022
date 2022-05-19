from tkinter import *

window = Tk()

left = Frame(window)
right = Frame(window)

left.grid(row=0, column=0)

texting1 = Label(right, text='right side, working').grid(row=0, column=0)
texting2 = Label(left, text='left side, working').grid(row=0, column=0)

def update():
    right.grid(row=0, column=1)

Button(left, text='update', command=update).grid(row=1, column=0)
