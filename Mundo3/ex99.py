#create a method to discover which values is the greatest between various integer values.

def great(num): #great(*num)
  maximum = max(num)
  print(f"The greatest value inputed is: {maximum}")

#main
num = []
length = int(input("How many values will you input?: "))
for i in range(0, length):
  value = int(input(f"{i+1}th value: "))
  num.append(value)
great(num)
