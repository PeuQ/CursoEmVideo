#checking parenteses
#input
expression = str(input("Input: "))

#program
p1 = expression.index('(')
p2 = expression.index(')')

if(p1 < p2):
  print("The parentheses are in the correct order.")
else:
  print("The parentheses are NOT in the correct order.")
