#base conversion

num = int(input("Enter a number: "))
choice = int(input("Choose the base for conversion:\n1 - Binary\n2 - Octadecimal\n3 - Hexadecimal\n"))
if(choice == 1):
  print("\n{}".format(bin(num)))
elif(choice == 2):
  print("\n{}".format(oct(num)))
elif(choice == 3):
  print("\n{}".format(hex(num)))
