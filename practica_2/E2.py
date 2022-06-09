

def getDatafromKeyboard():  # Funció que obté les dades per teclat
    text = input("Quin és el teu nom? ")
    return text


def positionLetter(text):
    lettersInText = {}
    count = 0
    for x in list(text):
        if x != " ":
            if x in lettersInText:
                savedPosition = lettersInText.get(x)
                newPosition = str(savedPosition) + ", " + str(count)
                lettersInText[x] = newPosition
            else:
                lettersInText[x] = count
            count += 1
    return lettersInText


def quantityOfLetters(lettersInText):
    lettersQuantity = {}
    for letter in lettersInText:
        lettersRepeated = str(lettersInText.get(letter))
        lettersQuantity[letter] = len(lettersRepeated.split(","))
    return lettersQuantity


def textSeparator():
    text = getDatafromKeyboard()
    print("Lletra\tQuantitat\tPosició")
    position = positionLetter(text)
    lettersQuantity = quantityOfLetters(position)
    for x in lettersQuantity:
        print(f"{x}\t\t{lettersQuantity.get(x)}\t\t\t{position.get(x)}")
