"""
Create a program to show how many "A"'s are in a strign as well as the first and last time it occurs.
"""

stnc = str(input("Your input: ")).upper().strip()
print("The letter 'A' shows up {} times".format(stnc.count('A')))
print("Its first occurrence is in index {}".format(stnc.find('A')))
print("Its last occurrence is in index {}".format(stnc.rfind('A')))
