#creata a function that functions as 'input()' but only for integers

#function def
def readInt(msg_input):
  num = str(input(msg_input))  
  if num.isnumeric():
    return num

#main
p = readInt("Input: ")

if p == None:
  print("You did not enter any number.")
else:
  print(f"You entered the number {p}.")
