
from tkinter import *

root = Tk()

enter_input_value = Entry(root, width=25, borderwidth=5 )
enter_input_value.pack()
enter_input_value.insert(0, "Type name here")

def myclick():
    myLabel = Label(root, text = "Hello "+ enter_input_value.get())
    myLabel.pack()

myButton = Button(root, text="Enter your name please : ", padx=45, pady=15, bg="grey", command=myclick)
myButton.pack()

root.mainloop()