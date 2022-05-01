#data from a list

lista = []
while True:
  n = float(input("input a number: "))
  lista.append(n)
  
  choice = str(input("Continuar?[S/N]: "))
  if(choice in 'Nn'):
    break

    
#How many numbers were inputed?
print("Number of inputs: {}".format(len(lista)))

##list in crescent order
lista.sort()
print("List in crescent order: {}".format(lista))

###is five in the list?
if('5' in lista):
  print("5 was inputed into the list")
else:
  print("5 is not in the list")
