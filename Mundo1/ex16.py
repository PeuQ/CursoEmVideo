#show the integer portion of a given number.

import math

num = float(input("Enter any number: "))

result = math.trunc(num)

print("The integer portion of the number is: {}".format(result))

"""
#no imports

print("The integer portion of the number is: {}".format(int(num)))

#shows only the integer portion
"""
