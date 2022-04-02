#program that plays jokenpo
import random

choice = str(input("Make your choice, rock, paper or scissors?: ")).lower()
comp_table = ['rock', 'paper', 'scissors']
comp_choice = random.choice(comp_table)

#player wins
if(choice == 'rock') and (comp_choice == 'scissors'):
  print("Comp: scissors")
  print("Player wins!")
elif(choice == 'paper') and (comp_choice == 'rock'):
  print("Comp: rock")
  print("Player wins!")
elif(choice == 'scissors') and (comp_choice == 'paper'):
  print("Comp: paper")
  print("Player wins!")
#computer wins
elif(choice == 'rock') and (comp_choice == 'paper'):
  print("Comp: paper")
  print("Computer wins!")
elif(choice == 'paper') and (comp_choice == 'scissors'):
  print("Comp: scissors")
  print("Computer wins!")
elif(choice == 'scissors') and (comp_choice == 'rock'):
  print("Comp: rock")
  print("Computer wins!")
else:
  print("It's a tie!")
