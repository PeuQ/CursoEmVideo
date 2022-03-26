#exemplo 1:
print("\033[4;36;47mHello, World!\033[m")

#exemplo 2:
print("\033[1;33;44m\nHello, World!\033[m")

#exemplo 3:
#Código 7 inverte as cores da letra e do fundo.
print("\033[7;33;44m\nHello, World!\033[m")

#exemplo 4:

print("\033[4;30;47m\nHello, World!\033[m")

#exemplo 5:
#Código 7 inverte as cores da letra e do fundo.
print("\033[7;30;47m\nHello, World!\033[m")

#exemplo 6: variáveis
a = 1
b = 2
print("\nOs valores de \033[31ma\033[m e \033[32mb\033[m são: \033[31m{}\033[m e \033[32m{}\033[m".format(a, b))

#exemplo 7:
nome = 'Pedro'
print("\nOlá! Prazer em te conhecer, {}{}{}.".format('\033[0;35m', nome, '\033[m'))

#exemplo 8: Dicionário de cores
nome = 'Pedro'
cores = {'limpa': '\033[m', 
        'vermelho': '\033[0;31m', 
        'verde': '\033[0;32m', 
        'ciano': '\033[0;36m', 
        'negativo': '\033[7;30;47m'}
print("\nOlá! Prazer em te conhecer, {}{}{} !!!".format(cores['ciano'], nome, cores['negativo']))
