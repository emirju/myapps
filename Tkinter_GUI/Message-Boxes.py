
from tkinter import *
from tkinter import messagebox

screen = Tk()
screen.title('Welcome to Cisco')
screen.iconbitmap('cisco.ico')
screen.geometry('300x150')

# There are several different types of boxes : 1.showinfo ; 2.showwarning ; 3.showerror ; 4.askquestion ; 5.askokcancel ; 6.askyesno
def popup():
    messagebox.showwarning("Configuration", "Config will be saved...")

Button(screen, text=" Save config ", command=popup, borderwidth=4).pack()


screen.mainloop()