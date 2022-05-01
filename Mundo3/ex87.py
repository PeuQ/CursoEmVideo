#matrix
matrix = [[0]*3 for i in range (3)]

#input
for i in range(0, 3):
  for j in range(0, 3):
    matrix[i][j] = int(input("Enter value to position [{}][{}]: ".format(i, j)))

for i in range(3):
  print(matrix[i])

#operations
sum_of_evens = 0
for i in range(3):
  for j in range(3):
    if(matrix[i][j] % 2 == 0):
      sum_of_evens += matrix[i][j]
print("The sum of all even values is {}".format(sum_of_evens))

sum_of_thirdcolumn = matrix[0][2] + matrix[1][2] + matrix[2][2]
print("The sum of values in the third column is {}".format(sum_of_thirdcolumn))

greatest_value_of_second_column = 0
#1st value
if(matrix[0][1] >= matrix[1][1] and matrix[0][1] >= matrix[2][1]):
  greatest_value_of_second_column = matrix[0][1]
#2nd value
elif(matrix[1][1] >= matrix[0][1] and matrix[1][1] >= matrix[2][1]):
  greatest_value_of_second_column = matrix[1][1]
  #3rd value
elif(matrix[2][1] >= matrix[0][1] and matrix[2][1] >= matrix[1][1]):
  greatest_value_of_second_column = matrix[2][1]
print("The greatest value of the second column is {}".format(greatest_value_of_second_column))
