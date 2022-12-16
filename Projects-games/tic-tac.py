import random 
from tkinter import *

def next_turn(row,column):
   
   global player

   if buttons[row][column]['text'] == "" and check_win() is False:  
      # the button that we have clicked is empty and the game has no winner yet then procede

      if player == players[0]: #first player is playing

         buttons[row][column]['text'] = player    
         buttons[row][column].config(bg='red')# red for player


         if check_win() is False:   #after first players strike there is no winner
            player = players[1]    #still no winner __> switch to next turn
            label.configure(text=(players[1]+" turn"))

         elif check_win() is True:   #check for winner (current player)from list is successful
            label.configure(text=(players[0]+" Wins!"))

         elif check_win() == "Tie" :       #neither true nor false it's tie
            label.configure(text="Tie!")
      
      else :#it's not player[0] player [1] is playing
         buttons[row][column]['text'] = player    
         buttons[row][column].config(bg='yellow')## yellow for second player


         if check_win() is False:   
            player = players[0]    
            label.configure(text=(players[0]+" turn"))

         elif check_win() is True:   
            label.configure(text=(players[1]+" wins!"))

         elif check_win() == "Tie" :       
            label.configure(text="Tie!")
   

def check_win():

   for row in range (3):  # for all horizontal conditions
      if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text']!= "" :
         #all the buttons are the same and not just blank spaces then we have a winner
         buttons[row][0].config(bg='green')
         buttons[row][1].config(bg='green')
         buttons[row][2].config(bg='green')
         return True

   for column in range (3):  # for all vertical conditions
      if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text']!= "" :
         #all the buttons are the same and not just blank spaces then we have a winner
         buttons[0][column].config(bg='green')
         buttons[1][column].config(bg='green')
         buttons[2][column].config(bg='green')
         return True

   if buttons [0][0]['text']==buttons [1][1]['text'] == buttons [2][2]["text"] !="":
      #winner along main digonal
      buttons [0][0].config(bg='green')
      buttons [1][1].config(bg='green')
      buttons [2][2].config(bg='green')
      return True
   elif buttons [2][0]['text']==buttons [1][1]['text'] == buttons [0][2]["text"] !="":
      #winner along minor diagonal
      buttons [2][0].config(bg='green')
      buttons [1][1].config(bg='green')
      buttons [0][2].config(bg='green')
      return True

   elif empty_spaces() is False :
     
      for row in range(3):
         for column in range(3):
            buttons[row][column].config(bg="grey")
      return "Tie"     #no winner= no spaces left

   else :       # there are spaces to fill but no winners yet
      return False



def empty_spaces():
   spaces = 9  #total blocks in our grid

   for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
               spaces -= 1  #if the box is not empty delete a space

   if spaces == 0:
        return False
   else:
        return True

def new_game():

    global player

    player = random.choice(players)

    label.configure(text=player+" turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#F0F0F0")



##############################################################################################
window =Tk() #name of our screen is window method is "Tk"
window.wm_title("Tic-Tac-Toe")#title of the screen(is not displayed)

players =['x','o']

player =random.choice(players)#randomly choose x or o player
print(player)

buttons =[[0,0,0],
          [0,0,0],
          [0,0,0]]


label = Label(text="Tic-Tac-Toe\n"+ player +" play !", font =("serif",30))  #basic text on the screen

label.pack(side="top")# managing text in the screen

reset_button = Button(text= "Restart game", font=("serif",20), command=new_game)#command takes you bac up to the function
reset_button.pack(side="bottom")#position reset button

frame =Frame(window,padx=10, pady=10,bg='black')
frame.pack()

for row in range(3):
   for column in range(3):
      buttons[row][column]= Button(frame,text="",font =("serif",40),height=2,width=5,
                                 command= lambda row=row ,column=column: next_turn(row,column)) 
                                 #lambda is an anonymous function
                                 #lambda takes only one expression but many arguments
      buttons[row][column].grid(row=row,column=column)


window.mainloop() # to keep the screen called window open 
#an infinite loop used to run the application, 


