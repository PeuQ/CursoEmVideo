#números por extenso.

contagem = ('zero', 'one', 'two', 'three', 'four', 'five',
           'six', 'seven', 'eight', 'nine', 'ten',
           'eleven', 'twelve', 'thirteen', 'fourteen', 'fithteen',
           'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')

number = int(input("give me a number between 1 and 20: "))

print("\nThats how you write it -> {}".format(contagem[number]))
