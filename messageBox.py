from tkinter import *
from tkinter import messagebox


window = Tk()
window.title("sign up")
window.geometry('350x200')

lbl1 = Label(window, text="Username")
lbl1.grid(column=0, row=0)

lbl2 = Label(window, text="Password")
lbl2.grid(column=0, row=1)

txt1 = Entry(window, width=10)
txt1.grid(column=1, row=0)

txt2 = Entry(window, show = '*', width=10)
txt2.grid(column=1, row=1)


def clicked():
    messagebox.showinfo('Welcom', 'Hello ' + txt1.get())
    

btn = Button(window, text="Submit", command=clicked)
btn.grid(column=2, row=2)

window.mainloop()