#show the first 10 numbers of an A.P.
a1 = float(input("Enter the A.P. First Term: ")) #first term.
d = float(input("Enter the Common Difference: "))

print("The first ten terms for this A.P. is:\n")
for n in range(1, 11):
  an = a1 + (n - 1)*d
  print(an)
