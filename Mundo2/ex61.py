#Arithmetic Progression V2

num = int(input("Enter the first term: "))
d = int(input("Enter the common difference: "))

new_term = num
i = 0
while i <= 9:
  if(i == 9):
    print("{}".format(new_term))
  else:
    print("{} -> ".format(new_term), end='')
  new_term += d
  i += 1
