#select a random student
import random

students = []

for i in range(0, 4):
  name = str(input("Enter the student's name: "))
  students.append(name)

print("The selected student is: {}".format(random.choice(students)))
