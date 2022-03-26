"""
Create a program that generates a random number beetween 0 and 5, and asks the user to guess which number is it.
"""
import random

num = random.randint(0, 5)
#print(num)

guess = int(input("Hey, I just thought of number! It's beetween 0 and 5, try to guess: "))

if(guess == num):
  print("Congratulations! You got it right.")
else:
  print("Sorry, you guessed wrong. The right answer is: {}".format(num))
