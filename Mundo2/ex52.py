# get a number anc check if its a prime number
num = int(input("Enter a number: "))
if(num < 0):
  print("Prime numbers are greater than 1. Please restart the program.")

for c in range(2, num): #this excludes '1' and 'itself' from the loop. since its a prime.
  if(num % c == 0):
    print("\nNo, {} is not a prime number.".format(num))
    break
  else:
    print("\nYes, {} is a prime number!".format(num))
    break
