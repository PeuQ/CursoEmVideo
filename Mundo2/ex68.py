#odds or even
import random
victories = 0
while True:
  sum = 0
  player = str(input("Odds or even?: ")).strip().lower()
  if(player == 'odds'):
    print("\nPlayer: Odds\nComp: Even")
    player_num = int(input("\nYour play(choose a number between 1 and 5): "))
    comp_num = random.randint(1, 5)
    print("Computer chose {}".format(comp_num))
    sum = player_num + comp_num
    if(sum % 2 == 0):
      print("You lose!")
      break
    else:
      victories += 1
      print("You win! Play again!")

  elif(player == 'even'):
    print("\nPlayer: Even\nComp: Odds")
    player_num = int(input("\nYour play(choose a number between 1 and 5): "))
    comp_num = random.randint(1, 5)
    print("Computer chose {}".format(comp_num))
    sum = player_num + comp_num
    if(sum % 2 == 0):
      victories += 1
      print("You win! Play again!")
    else:
      print("You lose!")
      break
print("You had {} consecutive victories\nend of program".format(victories))
