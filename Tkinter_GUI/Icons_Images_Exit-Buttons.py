
from tkinter import *

root = Tk()   #   screen = Tk();
root.geometry("420x320") ## size of screen   screen.geometry("420x320")

root.title(" Welcome to Cisco ")
root.iconbitmap('cisco.ico')


# EXIT button
quit_button = Button(root, text="Exit program" , command=root.quit, borderwidth=4)
quit_button.grid(row=10, column=10)

root.mainloop()

### from PIL import*
### for images there is 3 step proccess
# First one is : Define the image ; my_img = ImageTk.PhotoImage(Image.open('CiscoVisioLOGO.JPG'))

# Second one is : put image on something(this time on Label), we can have images on every Widges on tkinter
   # myLabel=Label(image=my_img)

# Third one is : Put this Label on the screen  ;  myLabel.pack()
