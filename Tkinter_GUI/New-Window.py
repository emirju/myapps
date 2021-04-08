
from tkinter import *

root=Tk()
root.title("Home page")
root.iconbitmap("cisco.ico")
root.geometry("400x300")


def open():
    top=Toplevel()  # Using TOPLEVEL insted of Tk(), so there will not be two versions of Tkinter(Tk); Toplevel is used for second window
    top.title("Second page")
    top.iconbitmap("cisco.ico")
    top.geometry("300x200")
    my_button = Button(top, text="Back to home page", command=top.destroy).pack()

btn=Button(root, text="Go to the next page", command=open).pack()


root.mainloop()