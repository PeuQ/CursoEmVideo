#player's chart: show the players chart even if some data hasn't been inputed correctly
#function def
def chart(name='[unknown]', points_made=0):
  print(f'the player {name} made {points_made} points in the match.')

#main
name = str(input('Enter the players name: '))
points = str(input('Enter how many points the player made: '))

if points.isnumeric():
  points = int(points)
else:
  points = 0

if name.strip() == "":
  chart(points_made = points)
else:
  chart(name, points)
