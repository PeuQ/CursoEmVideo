#compute the value of sin, cos, ad tangent for an angle.
import math

angle = float(input("Enter an angle in degrees: "))

radians = math.radians(angle)

sin = math.sin(radians)
cos = math.cos(radians)
tan = math.tan(radians)

print("For {} degrees, its sin is {:.2f}, its cos is {:.2f} and its tangent is {:.2f}".format(angle, sin, cos, tan))
