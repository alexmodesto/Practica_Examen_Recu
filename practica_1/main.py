from practica_1.ej1 import *
from practica_1.ej2 import *
from practica_1.ej3 import *
from practica_1.ej4 import *

def menu():
    """Esta funcion muestra el menu y da a elegir distintas funciones"""
    escollir = int(input('E1 (1)\nE2 (2)\nE3 (3)\nE4 (4)\n'))
    if escollir > 4:
        print('Escollir una opció valida')
    else:
        if escollir == 1:
            comptar_lletres()
        elif escollir == 2:
            mostrar_posicion_veces()
        if escollir == 3:
            canviar_ascii()
        if escollir == 4:
            printa_colors()
menu()




