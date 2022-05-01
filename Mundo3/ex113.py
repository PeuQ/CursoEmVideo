#create a function that functions as 'input()' but only for integers. do the same for floating point numbers and handle the exceptions. 

#function def
def readInt(msg_input):
    while True:
        try:
            n = int(input(msg_input))
        except (TypeError, ValueError):
            print("\033[0;31mAn error has ocurred! Please try a valid integer number.\033[m")
        except (KeyboardInterrupt):
            print("\033[0;31mOperation interrupted by user.\033[m")
            return 0
        else:
            return n

def readFloat(msg_input):
    while True:
        try:
            n = float(input(msg_input))
        except (TypeError, ValueError):
            print("\033[0;31mAn error has ocurred! Please try a valid floating point number.\033[m")
        except (KeyboardInterrupt):
            print("\033[0;31mOperation interrupted by user.\033[m")
            return 0
        else:
            return n

#main
number = readInt("Enter an integer number: ")
print(f"\033[0;32mYou entered the number {number}\033[m\n")

numberf = readFloat("Enter a floating number: ")
print(f"\033[0;32mYou entered the number {numberf}\033[m")
