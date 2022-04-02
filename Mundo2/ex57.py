sex = ''
get_sex1 = str(input("Are you a boy or a girl? \n"))
sex = get_sex1

if(sex != 'B') and (sex != 'G'):
  while(sex != 'B') and (sex != 'G'):
    get_sex2 = str(input("I don't understand, are you a boy or a girl(B or G)? \n")).upper().strip()
    sex = get_sex2

if(sex == 'B'):
  print("I see, a boy then.")
elif(sex == 'G'):
  print("I see, a girl then.")

"""
sex = str(iput("..."))
while sex not in 'MmFf':
  sex = str(input("..."))
print("blablabla")
"""
