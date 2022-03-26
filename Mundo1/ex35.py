#receive the size of three lines and tell if they can form a triangle.

a = int(input("Length of 'a': "))
b = int(input("Length of 'b': "))
c = int(input("Length of 'c': "))

#Checking Triangle Inequality Theorem:
if(a + b > c) and (a + c > b) and (b + c > a):
  print("These sides can form a triangle!")
else:
  print("Not possible to form a triangle.")
