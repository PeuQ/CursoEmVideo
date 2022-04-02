#athlete classification
age = int(input("Enters the athletes age: "))

if(age <= 9):
  print("LITTLE")
elif(age > 9) and (age <= 14):
  print("CHILD")
elif(age > 14) and (age <= 19):
  print("JUVINILE")
elif(age > 19) and (age <= 25):
  print("SENIOR")
else:
  print("MASTER")
