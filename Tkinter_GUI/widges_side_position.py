
from tkinter import *
root = Tk()

root.title('Button side position')
root.geometry('500x500')

left_button = Button(root, text='Red', fg='red',bd=10,font=5,height=5, width=12,activebackground = "black",activeforeground = "red")
left_button.pack(side=LEFT)

right_button = Button(root, text='Green', fg='green',bd=10,font=5,height=5, width=12)
right_button.pack(side=RIGHT)

top_button = Button(root, text='Black', fg='black',bd=10,font=5,height=5,width=12)
top_button.pack(side=TOP)

bottom_button = Button(root, text='Blue', fg='blue',bd=10,font=5,height=5,width=12)
bottom_button.pack(side=BOTTOM)

root.mainloop()