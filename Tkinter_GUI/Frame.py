
from tkinter import *
root = Tk()

frame = LabelFrame(root, text='This is my Frame', padx=20, pady=30, bd=14, relief='ridge') ##iner padx and pady IN THE FRAME
frame.pack(padx=35, pady=15)##outer padx and pady OUT OF THE FRAME

lbl = Label(frame, text='Click here to continue .. ').pack()

root.mainloop()

'''
 relief *** The relief style of a widget refers to certain simulated 3-D effects around the outside of the widget
  FLAT
  RAISED
  SUNKEN
  GROOVE
  RIDGE
'''