#programa que calcula quantos dólares uma pessoa pode comprar.

reais = float(input("Quantos reais você tem?: "))

# U$D1.00 = R$5.67
dolar = reais / 5.67

print("com R${} podes comprar U$D{:.2f}".format(reais, dolar))
