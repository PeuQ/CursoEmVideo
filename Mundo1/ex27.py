"""
Faça um programa que leia o nome completo de uma pessoa e a cumprimente com seu primeiro e último nome.
"""
nome = str(input("Como se chama?: ")).strip()
nome_lista = nome.split()
####
print("É um prazer te conhcer, {} {}!".format(nome_lista[0], nome_lista[len(nome_lista) - 1]))
