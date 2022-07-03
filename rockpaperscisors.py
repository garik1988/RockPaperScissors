from random import randint


def hand(choose): #ascii graphics creator
  options={1:"""         
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""", 2:"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",3:"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""" }
  return options.get(choose)


def winner(player,comp): #calculates winner
  result=""

  if player == comp:
    result="drawn"
    
  elif player == 1 and comp>2:
    result = "You Win"
    
  elif player == 2   and comp<2:
    result = "You Win"
 
  elif player == 3 and comp > 1:
    result = "You Win"
 
  else:
    result = "You Loose"
  


  return (result)






def main():
  comp=randint(1,3) #chooses rock,scissors,paper for computer rando
  
  playerscore =0 #player score
  
  compscore = 0 #computer score
  
  while True:  #mainloop
    print("1)Rock\n{}\n2)Paper\n{}\n3))Scissors\n{}".format(hand(1),hand(2),hand(3)))
    
    player=int(input("choose:"))
    
    print ("player\n{}\ncomputer\n{}".format(hand(player),hand(comp)))
    
    print(winner(player,comp),"\n")

    if winner(player,comp) == "You Win":
      playerscore+= 1
  
    if winner(player,comp) == "You Loose":
      compscore += 1
      
    print ("\t SCORE\n\n\nPlayer:{}\n\nComputer:{}\n".format(playerscore,compscore))
  
    playagain=input("do you want to play again? n/y:\nChoose: ")
    
    if playagain.capitalize()=="N":
      
      break
      
    elif playagain.capitalize() != "Y":
      
      print ("wrong option")

main()