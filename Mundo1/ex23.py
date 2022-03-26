"""
Create a program which reads a number and shows each digit on its own.
"""
num = int(input("Enter a number: "))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

print("\nUnidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}".format(unidade, dezena, centena, milhar))
