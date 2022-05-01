#sorted lists of even and odds
numbers = [[], []] #numbers[0] = evens, numbers[1] = odds

#input
for n in range(0, 7):
  n = int(input("Enter a number: "))
  if(n % 2 == 0):
    numbers[0].append(n)
  elif(n % 2 != 0):
    numbers[1].append(n)

#output
numbers[0].sort()
print("\nList of evens: {}".format(numbers[0]))

numbers[1].sort()
print("\nList of odds: {}".format(numbers[1]))
