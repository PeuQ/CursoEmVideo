#BMI calculator

height = float(input("Enter your height(centimeters): "))
weight = float(input("Enter your weight(Kg): "))
BMI = weight / (height/100)**2

if(BMI < 18.5):
  print("Underweight")
elif(BMI >= 18.5) and (BMI < 25):
  print("Ideal weight")
elif(BMI >= 25) and (BMI < 30):
  print("Overweight")
elif(BMI >= 30) and (BMI < 40):
  print("Obese")
else:
  print("Morbidly Obese")
