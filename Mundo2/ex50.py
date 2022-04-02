#receive 6 integers and output the sum of all evens

cont = 1
sum = 0
for n in range(0, 6):
  num = int(input("Enter the {}º number: ".format(n+1)))
  if(num % 2 == 0): #checking if its even
    sum += num

print(sum)