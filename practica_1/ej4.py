"""
Ex4
"""
from SystemColors_PP1 import *

vocals = {
    'a': CRED + 'a',
    'e': CYELLOW + 'e',
    'i': CBLUE + 'i',
    'o': CGREEN + 'o',
    'u': CBLACK + 'u',
    'A':CRED + 'A',
    'E':CYELLOW + 'E',
    'I':CBLUE + 'I',
    'O': CGREEN + 'O',
    'U': CBLACK + 'U',
}

def printa_colors():
    """Esta funcion canvia el color de las vocales"""
    nom = input('').split()
    for caracter in nom:
        for lletra in caracter:
            if lletra in vocals:
                print(vocals[lletra],end="")
            else:
                print(CRESET +lletra,end="")
