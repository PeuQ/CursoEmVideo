#create a program in which 4 players throw four dice, and their aleatory result is stored in a dictionary. Then, sort it and print it.
import random
from operator import itemgetter

#dicerolls for the players
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
dice3 = random.randint(1, 6)
dice4 = random.randint(1, 6)

#dictionary
players = {'player1': dice1, 'player2': dice2, 'player3': dice3, 'player4': dice4}

#sorting
players_list = sorted(players.items(), key = itemgetter(1),reverse = True)

#printing
print("High Score:\n")
for i, p in enumerate(players_list):
  print("{}º place: player {}, with {} on the dice.\n".format(i+1, p[0], p[1]))
  