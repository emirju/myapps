from tkinter import *
root = Tk()

root.config(bg='red')
root.geometry('300x250')

DAYs = [
    ("Monday","MON"),
    ("Tuesday","TU"),
    ("Wednesday","WED"),
    ("Thursday","THR"),
    ("Friday","FRI")
]

### show radion buttons
d=StringVar()
d.set('MON')### By this default option is Monday to print it use label
def_label_option=Label(root, text=d.get())  # By this we want to GET what is on the VARIABLE=D
def_label_option.pack()

for option, result_day in DAYs:
    Radiobutton(root, text=option, variable=d, value=result_day, bg='red').pack(anchor=W)
'''------------------------------------------------------------------------------------------'''

### When clicking on one of option wanna show some result
def clicked(value):
    my_label=Label(root, text=value)
    my_label.pack()

clicked_button=Button(root, text="Click here after you chose one option", bd=14, relief='raised', bg='yellow', command=lambda: clicked(d.get())).pack()

root.mainloop()