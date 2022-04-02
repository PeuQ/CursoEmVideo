#fibonacci v1 / firns N elements

N = int(input("How many elements would you like to see?: "))
t0 = 0
t1 = 1
print("{} -> {}".format(t0, t1), end='')
i = 3
while i <= N:
  t2 = t0 + t1
  print(" -> {}".format(t2), end='')
  t0 = t1
  t1 = t2
  i += 1
