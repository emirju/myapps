
### Option 1 for creating BUTTON WIDGET
from tkinter import *

root = Tk()

#creating a function for the button to do something
def myClick():
    myLabel = Label(root, text=" !!! You have successfully submited !!!")  #Creating a label
    myLabel.pack()  #Putting on the screen
## To execute this myClick function it has to be called by command=myClick


# myButton = Button(root, text=" Click here to accept conditions !!!")
# myButton = Button(root, text=" Click here to accept conditions !!!", padx=55, pady=30, state=DISABLED)
myButton = Button(root, text=" Click here to accept conditions !!!",command=myClick,  padx=55, pady=30, fg="black", bg="yellow")
                                                                                 #fg = foreground ; bg=background
myButton.pack()

root.mainloop()