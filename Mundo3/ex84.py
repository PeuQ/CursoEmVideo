#data from people
final_list = []
people_list = []
while True:
  name = str(input("What's your name?: "))
  weight = float(input("What's your weight?: "))
  people_list.append(name)
  people_list.append(weight)
  
  choice = str(input("Do you wish to continue?[S/N]: "))
  if(choice in 'Nn'):
    final_list.append(people_list)
    break
  else:
    final_list.append(people_list)
    people_list = []

#show number of registered people:
register = len(final_list)
print("The number of registered people is {}".format(register))

#heaviest people
heavy_list = []
for i in final_list:
  if i[1] >= 70: #threshold of 70 for being considered "heavy"
    heavy_list.append(i)

print("The heaviest people on the list are: {}".format(heavy_list))
#lightest people
light_list = []
for j in final_list:
  if j[1] < 70:
    light_list.append(j)

print("The lightest people on the list are {}".format(light_list))
