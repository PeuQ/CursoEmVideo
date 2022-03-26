#program to calculate how much pain is needed to paint a wall.

height = float(input("Enter the walls height(in meters): "))
length = float(input("Enter the walls length(in meters): "))

area = height * length

#1L of paint = 2m² of wall
paint_needed = area / 2

print("\nfor a wall with an area of {:.2f}m², it's necessary {:.2f}L of paint.".format(area, paint_needed))
