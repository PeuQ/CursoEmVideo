#Show the greater and the lower of three numbers.

num1 = float(input("1st Number: "))
num2 = float(input("2nd Number: "))
num3 = float(input("3rd Number: "))

#Finding the greater:
greater = 0
if(num1 >= num2) and (num1 >= num3):
  greater = num1
elif(num2 >= num1) and (num2 >= num3):
  greater = num2
elif(num3 >= num2) and (num3 >= num1):
  greater = num3

#findind the lowest:
low = 0
if(num1 <= num2) and (num1 <= num3):
  low = num1
elif(num2 <= num1) and (num2 <= num3):
  low = num2
elif(num3 <= num2) and (num3 <= num1):
  low = num3

#printinf result:
print("The greatest is: {:.2f}\nAnd the lowest is: {:.2f}".format(greater, low))
