#students grade

grade1 = float(input("Enter the 1st grade: "))
grade2 = float(input("Enter the 2nd grade: "))
final_grade = (grade1 + grade2) / 2

if(final_grade < 5.0):
  print("You've not been approved.")
elif(final_grade >= 5) and (final_grade <= 6.9):
  print("You must take the test again.")
elif(final_grade >= 7.0):
  print("You've beend approved.")
