#multiplication table

num = int(input("Enter a number to see its multiplication table: "))
for c in range(1, 11):
  print("{} x {} = {}".format(num, c, num*c))
