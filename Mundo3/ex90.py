#Read a students name and score to a dictinary, then print it.

student = dict()

student['name'] = str(input("Enter the student's name: "))
student['score'] = float(input("Enter the student's avarage score: "))

if(student['score'] >= 7):
  student['situation'] = 'approved'
elif(student['score'] >= 5 and student['score'] < 7):
  student['situation'] = 'in finals'
else:
  student['situation'] = 'rejected'

print("-"*30)
print("The student's name is {}.".format(student['name']))
print("Their avarage score is {}.".format(student['score']))
print("Thus their situation is '{}'.".format(student['situation']))
