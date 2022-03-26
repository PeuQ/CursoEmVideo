#write a program that reads a value in metres and transforms it to centimeters and milimeters.

num = float(input("Enter a value in meters: "))

centi = num * 100

mili = num * 1000

print("{0}m is equivalent to {1}cm and to {2}mm".format(num, centi, mili))
