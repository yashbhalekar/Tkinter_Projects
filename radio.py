#RADIO BUTTONS

from tkinter import *
window =Tk()
window.title("Radio Buttons")
window.iconbitmap("favicon.ico")


#DECLARING Tkinter VARIABLE
r = StringVar()
r.set("1")

#DEFINING A FUNTION TO  GET VALUE
def clicked(value):
    myLabel = Label(window, text=value).pack()



#  CREATING RADIO BUTTON
Radiobutton(window , text="Option1" , variable=r ,value="mango" ).pack()
Radiobutton(window , text="Option2" , variable=r ,value="orange").pack()
Radiobutton(window , text="Option3" , variable=r ,value="banana").pack()
Radiobutton(window , text="Option4" , variable=r ,value="apple").pack()

#CREATING A LABEL TO GET VALUE
#myLabel =Label(window , text=r.get()).pack()

#CREATING A SUBMIT BUTTON
button1= Button(window , text="submit" ,command=lambda :clicked(r.get())).pack()

window.mainloop()