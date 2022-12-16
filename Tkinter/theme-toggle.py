from tkinter import *
#importing only a part of the GUI library

def on_click():

   global mode
   
   if mode:
      #if switch_mode is true then it means that the active mode is light
      switch.config(image=dark,bg="black",activebackground="black")
      mode=False
   else :
      switch.config(image=light, bg="white",activebackground="white")
      mode=True




window = Tk()
window.title("Switch mode")
#window.geometry("500x300")


dark =PhotoImage (file="images/dark_mode.png")
light= PhotoImage(file= "images/light_mode.png")

mode=True


switch= Button(window,image=light ,bg="white",activebackground="white", command=on_click)
#we are not passing any arguments hence we do not need any parenthesis for on_click function
switch.pack(side="top")


window.mainloop()

