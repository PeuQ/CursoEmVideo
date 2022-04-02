#get the wight of 5 people and show which is the lightest and wich is the heaviest.
heavy = 0
light = 0

#input and comparisons
for i in range(0, 5):
  weight = float(input("Enter the {}° persons weight(Kg): ".format(i+1)))
  if(i == 0):
    heavy = weight
    light = weight
  else:
    if(weight > heavy):
      heavy = weight
    elif(weight < light):
      light = weight

print("The greatest weight inputed was {}Kg\nAnd, the lowest was {}Kg.".format(heavy, light))
