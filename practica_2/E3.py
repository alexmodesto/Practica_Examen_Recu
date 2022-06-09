def getDatafromKeyboard():  # Funció que obté les dades per teclat:
    text = input("Quin és el teu nom? ")
    return text

def asciiConverter(text):   # Funció que converteix a ASCII
    convertedTextList = []
    for letter in text:
        convertedLetter = ord(letter)
        convertedTextList.append(convertedLetter)
    convertedText = ".".join(str(e) for e in convertedTextList)
    return convertedText


def convertedText():
    text = getDatafromKeyboard()
    result = asciiConverter(text)
    return result

