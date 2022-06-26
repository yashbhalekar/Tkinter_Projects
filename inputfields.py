from tkinter import *

window =Tk()

e = Entry(window ,width=50)
e.pack()
e.insert(0 ,"Enter Your Name")

def myClick():
    myLabel =Label(window , text =e.get() )
    myLabel.pack()


button1= Button(window , text="Enter Your Name" , command=myClick)
button1.pack()

window.mainloop()