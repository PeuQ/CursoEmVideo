"""
Write a program that receives the speed of car and gives tickets if the speed is above the  limit.
"""

speed = float(input("Car speed(in Km/h): "))

#speed limit = 80Km/h
if(speed <= 80):
  print("...")
else:
  print("You're above the speed limit!\nYou will receive a fine of ${:.2f}".format((speed - 80) * 7))
  #fine is $7 for every Km/h above the limit.
