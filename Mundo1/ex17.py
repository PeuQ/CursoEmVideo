#compute the hypotenuse for a right triangle
import math

x = float(input("Enter the base side: "))

y = float(input("Enter the perpendicular side: "))

hypot = math.hypot(x, y)

print("The hypothenuse for this triangle is {:.2f}".format(hypot))
