from E1 import *


#from E4 import *


def menuOptions():
    print("\n[0] Comptador de lletres\n"
          "[1] Calculador de vocals i consonants\n"
          "[2] Convertir ASCII\n"
          "[3] Vocals en colors\n"
          "[4] Executar tot\n"
          "[S] Sortir")

def selectedOption():
    option = str(input())
    return option

def menu(option):
    while option.upper() != "S":
        if option == "1":
            option = ""
            lettercount()


def runMenu():
    menuOptions()
    option = selectedOption()
    menu(option)

runMenu()
