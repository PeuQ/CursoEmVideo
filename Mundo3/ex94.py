#Create a program that reads the name, sex and age of several people, storing each person's data in a dictionary and all dictionaries in a list. At the end, show: A) How many people were registered B) The average age C) A list of women D) A list of people older than average.

#getting data
dict = {}
people = []
answer = 'y'
while(answer == 'y' or answer == 'Y'):
  dict.clear()
  dict['name'] = str(input("Name: "))
  dict['sex'] = str(input("Sex(M/F): "))
  dict['age'] = int(input("Age: "))
  people.append(dict.copy())
  answer = str(input("\nInput another person?(y/n): "))

#showing answers

#A)
print("{} people were registered.".format(len(people)))

#B)
sum = 0
for i in range(0, len(people)):
  temp = people[i]['age']
  sum += temp
avg_age = sum/len(people)
print("The avarage age of the group is {:.2f}".format(avg_age))

#C)
print("\nThe list of women is: ")
for m in people:
  if(m['sex'] in 'fF'):
    print("{}".format(m['name']), end=', ')

#D)
print("\n\nThe list of people older than avarage is: ")
for o in people:
  if(o['age'] > avg_age):
    print("{}".format(o['age']), end=', ')
