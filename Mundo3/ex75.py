#tuples
numbers = (int(input("input a number: ")), int(input("input a number: ")), int(input("input a number: ")), int(input("input a number: ")))

print("You inputed the values {}".format(numbers))
print("The number 9 appeared {} times\nThe first '3' is in position {}".format(numbers.count(9), numbers.index(3)+1))
print("The even values are ", end='')
for n in numbers:
  if n % 2 == 0:
    print(n, end='')
