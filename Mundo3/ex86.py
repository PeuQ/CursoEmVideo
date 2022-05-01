#matrix
matrix = [[0]*3 for i in range (3)]

#input
for i in range(0, 3):
  for j in range(0, 3):
    matrix[i][j] = int(input("Enter value to position [{}][{}]: ".format(i, j)))

for i in range(3):
  print(matrix[i])
