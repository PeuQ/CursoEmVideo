#Arithmethic Progression V3

num = int(input("Enter the first term: "))
d = int(input("Enter common difference: "))

new_term = num
i = 0
while i < 10:
  if(i == 9):
    print("{}".format(new_term))
  else:
    print("{} -> ".format(new_term), end='')
  new_term += d
  i += 1

c = 1
while c > 0:
  more_terms = int(input("\nHow many more terms would you like to see?(type 0 to end program): "))
  if(more_terms != 0):
    i = 0
    while i < more_terms:
      if(i == (more_terms - 1)):
        print("{}".format(new_term))
      else:
        print("{} -> ".format(new_term), end='')
      new_term += d
      i += 1
  else:
    print("")
    c -= 1
