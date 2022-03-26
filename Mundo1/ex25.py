"""
Crie um programa que leia o nome de uma pessoa e diga se ela tem silva no nome.
"""

nome = str(input("Qual é seu nome completo? ")).strip()
print("SILVA" in nome.upper())
