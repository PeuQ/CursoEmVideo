def makeLine(tam=45):
    return '-' * tam


def headliner(text):
    print(makeLine())
    print(text.center(45))
    print(makeLine())

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

def menu(menu_list):
    headliner("\033[34mMAIN MENU\033[m")
    counter = 1
    for item in menu_list:
        print(f'\033[33m{counter}\033[m - \033[34m{item}\033[m')
        counter += 1
    print(makeLine())
    option = readInt("What do you wish to do?: ")
    return option
