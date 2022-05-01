#enhance ex93
##Create a program to track various players scores. It must receive the player's name, and how many matches they played. Then it must receive how many goals they made in each match, and store it all in a dictionary.

#player data
player = {}
goals = []
team = []
while True:
  player.clear()
  player['name'] = str(input("Enter player's name: "))
  player['matches'] = int(input("Enter how many matches they played: "))
  sum = 0
  goals.clear()
  for i in range(0, player['matches']):
    goals.append(int(input("How many goals in the {}º match?: ".format(i+1))))  
    sum += goals[i]
  player['goals'] = goals[:]
  player['sum'] = sum
  team.append(player.copy())
  while True:
    answer = str(input("Continue?:[Y/N] ")).upper()[0]
    if answer in 'YN':
      break
    print("ERROR! Answer must be Y or N.")
  if answer == 'N':
    break

#printing
print('-'*40)
print("cod", end=' ')
for i in player.keys():
  print(f'{i:<15}', end='')
print("\n")

print('-' * 40)
for k, v in enumerate(team):
  print(f'{k:>3}', end=' ')
  for d in v.values():
    print(f'{str(d):<15}', end='')
  print()
print('-' * 40)

#user search:
while True:
  search = int(input("Show which players data?:(999 for stopping search) "))
  if search == 999:
    break
  if search >= len(team):
    print(f'ERROR! there are no players with search code {search}.')
  else:
    print(' -- Player: {}'.format(team[search]['name']))
    for i, j in enumerate(team[search]['goals']):
      print(f"{i+1}* match: {j} goal.")
  print("-"*40)
print("\n")
