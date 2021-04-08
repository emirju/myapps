
from tkinter import *

root = Tk()

#Creating a Label Widget
myLabel1 = Label(root, text="Welcome to Tkinter")
myLabel2 = Label(root, text="My name is Emir Jukovic")
myLabel3 = Label(root, text=" !-!     !-! ").grid(row=1, column=1)

#Showing it onto the screen !!!
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=2)
#myLabel3.grid(row=1, column=1)

root.mainloop()