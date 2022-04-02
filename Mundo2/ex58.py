#try tp guess the randomly generated number
import random
num = random.randint(0, 10)
print(num)
choice = int(input("Try to guess the number! It's between 1 and 10: "))
attempts = 1
while(choice != num):
  choice = int(input("Try again!: "))
  attempts += 1
print("Thats right you got it! The number was {}".format(num))
print("And, you needed {} attempt(s) to get it right.".format(attempts))
