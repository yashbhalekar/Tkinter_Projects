from tkinter import *
from tkinter import  messagebox

window = Tk()
window.title("box")

def select():
    response =messagebox.askyesno( "Question Displayed", "Do you want to Exit")
    myLabel =Label(window ,text=response).pack()

    if response == 1:
        Label(window , text="Yes").pack()
    else:
        Label(window ,text="No").pack()

Button(window , text="Click Here" ,command=select).pack()

window.mainloop()