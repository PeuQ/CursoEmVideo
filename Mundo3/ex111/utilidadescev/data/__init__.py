def readValue(msg):
    valid = False
    while not valid:
        userInput = str(input(msg)).replace(',', '.')
        if userInput.isalpha().strip():
            print(f"Invalid input: '{userInput}'. Try Again.")
        else:
            valid = True
            return float(userInput)
