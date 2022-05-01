from lib.interface import *
from time import sleep
from lib.file import *
fileName = "ex115/datatest.txt"

if fileExists(fileName):
    print("\nFile Loaded Successfully!")
else:
    print("\nFile not loaded. ERROR!")
    createFile(fileName)


headliner("ARCHIVE SYSTEM V1.0\n")
while True:
    response = menu(["Register User", "List Registers", "End Operations"])
    if response == 1:
        #register a new user in the file
        headliner("REGISTER NEW USER")
        userName = str(input("Name: "))
        userAge = readInt("Age: ")
        registerUser(fileName, userName, userAge)
    elif response == 2:
        #list the content of a file
        readFile(fileName)
    elif response == 3:
        #terminated system operation
        print("SYSTEM TERMINATED")
        break
    else:
        print(f"\033[31mAn Error has ocurred. Please enter a valid option.\033[m\n")
    sleep(1)
