"""
    Àlex Modesto Mena
    Recuperació UF2 ASIXc 1B
    10/06/2022
    Menu
"""

from ej1 import *
from ej2 import *

def menu():
    escollir = int(input('E1 (1)\nE2 (2)\nE3 (3)\n'))
    if escollir > 3:
        print("Opcion no valida!")
    else:
        if escollir == 1:
            comptador()
        elif escollir == 2:
            mostrar_posicio()
        if escollir == 3:
            print("Exercici no aconseguit")

menu()
