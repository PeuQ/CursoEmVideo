import random
numbers = []

def randomDraw5():
  for n in range(0, 5):
    n = random.randint(0, 1000)
    numbers.append(n)

def evenSum(intlist):
  sum = 0
  for i in range(0, 5):
    if(intlist[i]%2 == 0):
      sum += intlist[i]
  return sum

#main
randomDraw5()
sum_result = evenSum(numbers)

print(f"The generated list is: {numbers}\n")
print(f"While the summation of its even numbers is: {sum_result}")
