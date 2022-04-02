#factorial

num = int(input("Enter a number: "))
fact = 1
print("{}! = ".format(num), end='')
while(num != 0):
  print("{}".format(num), end='')
  if num > 1:
    print(' x ', end='')
  else:
    print(' = ', end='')
  fact *= num
  num -= 1
print("{}".format(fact))

"""
from math import factorial
n = int(input("blablabla"))
f = fact(n)
print(f)
"""
