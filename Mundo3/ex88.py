#lotterry tickets
import random
game = []
all_games = []

number_of_games = int(input("How many games will you play?: "))
for i in range(number_of_games):
  for j in range(0, 6):
    n = random.randint(1, 60)
    game.append(n)
  
  all_games.append(game)
  game = []

print("\nYour suggested games for the lottery are:\n {}".format(all_games))
