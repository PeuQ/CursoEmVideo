#Create a program to track a players score. It must receive the player's name, and how many matches they played. Then it must receive how many goals they made in each match, and store it all in a dictionary.

#making the dictioinary
dict = {}
goals = []

dict['name'] = str(input("Enter player's name: "))
dict['matches'] = int(input("Enter how many matches they played: "))
sum = 0
for i in range(0, dict['matches']):
  goals.append(int(input("How many goals in the {}º match?: ".format(i+1))))  
  sum += goals[i]
dict['goals'] = goals[:]
dict['sum'] = sum

#printing
print('-'*30)
print("Player {} participated in {} matches\n".format(dict['name'], dict['matches']))
for j in range(0, dict['matches']):
  print("In the {}º match, they scored {} goal(s)\n".format(j+1, dict['goals'][j]))
print("Total score: {} goals".format(dict['sum']))
