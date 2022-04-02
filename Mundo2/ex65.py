#
sum = 0
how_many = 0
greatest = 0
lowest = 0
flag = 1

choice = str(input("Would you like to enter the first number?[y/n]: "))
if choice == 'y':
  num = int(input("Enter the first number: "))
  sum += num
  how_many += 1
  greatest = num
  lowest = num
  while flag != 0:
    choice = str(input("Would you like to enter the next number?[y/n]: "))
    if choice == 'n':
      print("The total sum is {}\n{} numbers were inputed\n{} was the greatest\n{} was the lowest".format(sum, how_many, greatest, lowest))
      flag = 0
    elif choice == 'y':
      num = int(input("Enter the next number: "))
      sum += num
      how_many += 1
      if(num > greatest):
        greatest = num
      elif(num < lowest):
        lowest = num
elif choice == 'n':
  print("A total of 0 numbers were entered.")
