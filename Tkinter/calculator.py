from tkinter import *

screen =Tk()
screen.title("Calculator")

frame=Frame(screen,bg="grey")
frame.pack()

head=Label(screen,text="Simple Calculator",font=("sans serif",30))
head.pack(side="top")

keys=[[0],[0],[0],
      [0],[0],[0],
      [0],[0],[0]]

for row in range (4):
   for col in range (4):
      keys[row][col] = Button(screen,text="k",height=3,width=3)
      keys.grid(row=row,column)

screen.mainloop()