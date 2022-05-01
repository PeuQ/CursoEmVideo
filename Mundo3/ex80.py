#no sort ordered list
lista = []
count = 0

for i in range(0, 5):
  n = int(input("input {} number: ".format(count+1)))
  if i == 0 or n > lista[-1]: #lista[-1] representa ultimo valor da lista
    lista.append(n)
    count += 1
  else:
    pos = 0
    while pos < len(lista):
      if n <= lista[pos]:
        lista.insert(pos, n)
        break
      pos += 1

print("="*40)
print("A lista ordenada é: {}".format(lista))
