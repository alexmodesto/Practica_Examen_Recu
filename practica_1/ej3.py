"""
Ex3
"""
from practica_1.ej2 import *
#TODO:Eliminar el puno final al printar
def canviar_ascii():
    """Esta funcion intercanvia el caracter por el valor ascii"""
    a = agafar_nom()
    for i in a:
        print(ord(i),end=".")


