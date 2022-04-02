#menu building and usage
num1 = float(input("Enter the 1st value: "))
num2 = float(input("Enter the 2nd value: "))

choice = 0
while(choice != 5):
  choice = int(input("\nWhat would you like to do?:\n[1]Sum\n[2]Multiply\n[3]Greater\n[4]New Input\n[5]End Program\nYour choice: "))

  if(choice == 1):
    sum = num1 + num2
    print("The sum is {}".format(sum))
  elif(choice == 2):
    result = num1 * num2
    print("The result of multiplication is {}".format(result))
  elif(choice == 3):
    if(num1 > num2):
      print("{} is greater.".format(num1))
    elif(num1 < num2):
      print("{} is greater.".format(num2))
    else:
      print("They are equal.")
  elif(choice == 4):
    num1 = float(input("Enter the 1st value again: "))
    num2 = float(input("Enter the 2nd value again: "))
    print("The new values are {} and {}".format(num1, num2))
  elif(choice > 5):
    print("Invalid choice. Try again.")

print("Program terminated...")
