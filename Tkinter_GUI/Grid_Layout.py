
from tkinter import *

root = Tk()

root.title('Cisco credentials')
root.iconbitmap('cisco.ico')
root.geometry("270x150")
root.configure(background='black')

label_1 = Label(root, text='Name : ',bg='black', fg='white')
label_2 = Label(root, text='Password : ', bg='black', fg='white' )

label_1.grid(row=0, pady=20)
label_2.grid(row=1, pady=10)

entry_1 = Entry(root, borderwidth=4, width=30)
entry_2 = Entry(root, borderwidth=4, width=30)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

check_but_1=Checkbutton(root, text='Keep me logged in !!! ', bg='black', fg='white')
check_but_1.grid(columnspan=2, pady=10)


root.mainloop()