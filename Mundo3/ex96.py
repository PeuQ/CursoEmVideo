#create a method to calculate the area of a rectangle

#method
def area(length, height):
  result = length * height
  print("The area of the {:.2f} x {:.2f} terrain is {:.2f}m²".format(length, height, result))
  
#main
print('-'*40)
print("TERRAIN AREA CALCULATION")
print('-'*40)
print("\n")

length = float(input("What's the length of the terrain?: "))
height = float(input("What's the height of the terrain?: "))
print("\n")

area(length, height)
