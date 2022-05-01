#greatest and lowest value in list

numbers = []
for n in range(0, 5):
  n = int(input("Enter a number: "))
  numbers.append(n)
#print(numbers)
print("\nGreatest number: {}\nLowest number: {}".format(max(numbers), min(numbers)))
