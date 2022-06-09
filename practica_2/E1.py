

def getDatafromKeyboard():  # Funció que obté les dades per teclat:
    text = input("Quin és el teu nom? ")
    return text

def letterCounter(text):
    count = 0
    for letter in list(text):
        if letter.isalpha():
            count += 1
    return count


def lettercount():
    letterCounter(getDatafromKeyboard())
