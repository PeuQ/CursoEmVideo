#method definition
def factorial(num, show=False):
  fact = 1
  for i in range(num, 0, -1):
    if show:
      print(f"{fact} x ", end='')
      fact *= i
  return fact
#main
num = int(input("To which number do you wish to get the factorial?: "))
factorial(num)
factorial(num, show=True)
