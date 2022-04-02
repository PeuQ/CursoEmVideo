#sum of all even numbers multiples of 3 between 1 and 500
sum = 0
for n in range(1, 501, 2):
  if(n % 3 == 0):
    sum += n
print("the sum of all numbers multiples of 3 between 1 and 500 is: {}".format(sum))
