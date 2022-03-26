"""
Program to calculate the price of a trip.
"""
dist = float(input("How far is your destination(in Km): "))
#prices:
#distance <= 200 => $0.5/Km
#distance > 200 => $0.45/Km
if(dist <= 200):
  print("Your trip will cost ${:.2f}".format(dist * 0.50))
elif(dist > 200):
  print("Your trip will cost ${:.2f}".format(dist * 0.45))
