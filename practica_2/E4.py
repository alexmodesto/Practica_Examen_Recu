vowels = ["a", "á", "à", "é", "è", "e", "i", "ï", "í", "ì", "o", "ó", "ò", "u", "ü", "ú", "ù"]

def getDatafromKeyboard():  # Funció que obté les dades per teclat:
    text = input("Quin és el teu nom? ")
    return text

def changeColor(text):
    for x in list(text):
        if x in vowels:
            if x == "a" == "á" == "à":
                print('\33[30m' + x, end="")
            elif x == "é" == "è" == "e":
                print('\33[31m' + x, end="")
            elif x == "i" == "ï" == "í" == "ì":
                print('\33[32m' + x, end="")
            elif x == "o" == "ó" == "ò":
                print('\33[33m' + x, end="")
            else:
                print('\33[34m' + x, end="")
        else:
            print(x, end="")

def colorChanger():
    text = getDatafromKeyboard()
    changeColor(text)

colorChanger()

