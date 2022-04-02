#receive the size of three lines and tell if they can form a triangle. Show which kind of triangle it is.

a = int(input("Length of 'a': "))
b = int(input("Length of 'b': "))
c = int(input("Length of 'c': "))

#Checking Triangle Inequality Theorem:
if(a + b > c) and (a + c > b) and (b + c > a):
  print("These sides can form a triangle!")
  #Checking the kind of triangle it is:
  if(a == b == c):
    print("EQUILATERAL")
  elif(a == b != c) or (a == c != b) or (b == c != a):
    print("ISOCECELES")
  elif(a != b != c):
    print("SCALENE")

else:
  print("Not possible to form a triangle.")
