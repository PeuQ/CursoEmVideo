from lib.interface import *


def fileExists(fileName):
    try:
        a = open(fileName, 'rt') # rt == readtext
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def createFile(fileName):
    try:
        a = open(fileName, 'wt+') #wt = writetext | + = if there is no file it makes one.
        a.close()
    except:
        print("Could not create file.")
    else:
        print(f"file {fileName} created successfully!")


def readFile(fileName):
    try:
        a = open(fileName, 'rt')
    except:
        print("ERROR! Unable to read file.")
    else:
        headliner("REGISTERED USERS")
        for line in a:
            data = line.split(";")
            data[1] = data[1].replace("\n", "")
            print(f"{data[0]:<30}{data[1]:>3}")
    finally:
        a.close()


def registerUser(fileName, userName, userAge):
    try:
        a = open(fileName, 'at') #apendtext
    except:
        print("ERROR! unable to open file.")
    else:
        try:
            a.write(f"{userName};{userAge}\n")
        except:
            print("ERROR! unable to write in file.")
        else:
            print(f"User {userName} is now registered.")
    finally:
        a.close()
