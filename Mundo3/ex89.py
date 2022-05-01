#class report card
student = []
report_card = []
while True:
  name = str(input("Name of the student: "))
  student.append(name)
  
  grade1 = float(input("1st grade of the student: "))
  student.append(grade1)
  
  grade2 = float(input("2nd grade of the student: "))
  student.append(grade2)

  report_card.append(student)
  student = []
  
  choice = str(input("More students?[Y/N]: "))
  if(choice in 'Nn'):
    break

print("="*30)
print("Class Report Card")
print("="*30)
for s in report_card:
  final_grade = (s[1] + s[2])/2
  print("{} -> Final Grade: {}\n".format(s[0], final_grade))

choice2 = str(input("See a students grades?[Y/N]: "))
if(choice2 in "Yy"):
  while True:
    student_name = str(input("From which student? "))
    for s in report_card:
      if(s[0] == student_name):
        print(s)
  
    choice3 = str(input("See another students grades?[Y/N]: "))
    if(choice3 in 'Nn'):
      print("Program Terminated.")
      break
