"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
"""
ages_sum = 0
oldest_man_name = ''
oldest_man_age = 0
women_under_20 = 0

for p in range(0, 4):
  name = str(input("{}° persons name: ".format(p+1))).strip()
  age = int(input("{}° persons age: ".format(p+1)))
  sex = str(input("{}° persons sex(M or F): ".format(p+1))).upper().strip()
  print("\n")
  
  ages_sum += age
  if(sex == 'M'):
    if(age > oldest_man_age):
      oldest_man_name = name
  elif(sex == 'F'):
    if(age < 20):
      women_under_20 += 1

avarage_age = ages_sum / 4
print("The avarage age of the group is {}.".format(avarage_age))
print("The oldest man name is {}".format(oldest_man_name))
if(women_under_20 > 1):
  print("And, there are {} women under 20 in the group".format(women_under_20))
else:
  print("And, there is {} woman under 20 in the group".format(women_under_20))
