from datetime import date

dict = {}

#coleta de dados
dict['nome'] = str(input("Seu nome: "))
dict['nascimento'] = int(input("Ano de nascimento: "))
ano_atual = date.today().year
dict['idade'] = ano_atual - dict['nascimento']
dict['CTPS'] = int(input("Número da sua carteira de trabalho: "))

if(dict['CTPS'] != 0):
  dict['contratação'] = int(input("Ano de contratação: "))
  dict['salario'] = float(input("Salário: "))
  dict['aposentadoria'] = dict['idade'] + ((dict['contratação'] + 35) - date.today().year) #35 =~ tempo de trabalho em anos
print('-'*30)
print("{} vai se aposentar com {} anos".format(dict['nome'], dict['aposentadoria']))
print("\nDados completos:")
for k, v in dict.items():
  print("{} tem valor {}".format(k, v))
