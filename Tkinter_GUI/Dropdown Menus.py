from tkinter import *

root = Tk()
root.geometry('200x200')

days_in_week = [     ## this is a list
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday'
]
clicked = StringVar()
clicked.set(days_in_week[0])  # By this Monday will be default value from list showed on dropdown menu

dropdown_menu = OptionMenu (root, clicked, *days_in_week)  # clicked is variable , *days_in_week is a list
dropdown_menu.pack(anchor=W, padx=25, pady=15)

def selected():
    mylabel=Label(root,text=clicked.get())
    mylabel.pack()

mybutton = Button(root,text="Show selection day", command=selected).pack()



root.mainloop()