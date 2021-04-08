
from tkinter import *
window=Tk()

b = Button (window,text='ERROR', bitmap='error').pack()
b = Button (window, bitmap='gray75').pack()
b = Button (window, bitmap='gray50').pack()
b = Button (window, bitmap='gray25').pack()
b = Button (window, bitmap='gray12').pack()
b = Button (window, bitmap='hourglass').pack()
b = Button (window, bitmap='info').pack()
b = Button (window, bitmap='questhead').pack()
b = Button (window, bitmap='question').pack()
b = Button (window, bitmap='warning').pack()

window.mainloop()

'''
The following below are the types of bitmaps available :
    error
    gray75
    gray50
    gray25
    gray12
    hourglass
    info
    questhead
    question
    warning
'''