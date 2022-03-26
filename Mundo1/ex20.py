#show the order in which the students were chosen
import random
students = []

for i in range (0,4):
    name = str(input("Enter the student's name: "))
    students.append(name)
  
print("\n")

for j in range(0,4):
    chosen = random.choice(students)
    print("The {}º student is: {}".format(j+1, chosen))
    students.remove(chosen)

"""
#shuffle method
import random

students = []

for i in range (0,4):
    name = str(input("Enter the student's name: "))
    students.append(name)

random.shuffle(students)

print(students)
"""
