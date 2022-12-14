import random 
from tkinter import *

def next_turn():
   pass

def check_win():
   pass

def empty_spaces():
   pass

def new_game():
   pass

window =Tk() #name of our screen is window method is "Tk"
window.wm_title("Tic-Tac-Toe")#title of the screen

players =["x","o"]

player =random.choice(players)#randomly choose x or o player

buttons =[[0,0,0],
         [0,0,0],
         [0,0,0]]

label = Label(text= player+" play !", font =("comicsans",40))  #basic text on the screen

label.pack(side="top")# managing text in the screen

reset_button = Button(text= "Restart game", font=("comicsans",20), command=new_game)#command takes you bac up to the function
reset_button.pack(side="top")#position reset button


window.mainloop() # to keep the screen called window open 
#an infinite loop used to run the application, 

frame =Frame(window)
frame.pack()