#various values and a flag

num = 0
how_many = 0
sum = 0
while num != 999:
  num = int(input("Which number now?(type 999 for final results): "))
  if(num == 999):
    break
  sum += num
  how_many += 1

print("{} numbers were typed, and their sum is {}.".format(how_many, sum))
