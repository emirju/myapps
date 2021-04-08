
from tkinter import *

root = Tk()
root.geometry('300x300')

v=IntVar()
v.set('1')  # Default value will be set to 1
#Function for value options
def clicked_option(value):
    my_label=Label(root,text=value)
    my_label.pack()

Radiobutton(root, text='Option - 1', variable=v, value=1, command= lambda: clicked_option(v.get())).pack(anchor=W)
Radiobutton(root, text='Option - 2', variable=v, value=2).pack(anchor=W)

default_value = Label(root, text=v.get()).pack() # Label created to display default value

## Creating button which will display option numbers
my_button = Button(root, text="Click to display button option", command=lambda: clicked_option(v.get())).pack()

root.mainloop()