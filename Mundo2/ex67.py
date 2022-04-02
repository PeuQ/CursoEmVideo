#multiplication table v3.0
#stop the table when input is negative
num = 0
while num >= 0:
  if(num < 0):
    break
  num = int(input("Show the multiplication table for: "))
  cont = 1
  while cont <= 10:
    print("{} x {} = {}".format(num, cont, num * cont))
    cont+= 1
  print("\n")
print("end of program")
