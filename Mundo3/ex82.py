#divinding values
lista1 = []
lista2 = []
lista3 = []

while True:
  n = float(input("input a number: "))
  lista1.append(n)
  if(n % 2 == 0):
    lista2.append(n)
  elif(n % 2 != 0):
    lista3.append(n)    
  choice = str(input("Continue?[S/N]: "))
  if(choice in "Nn"):
    break

print("Full list: {}".format(lista1))
print("Evens: {}".format(lista2))
print("Odds: {}".format(lista3))
