"""
    Àlex Modesto Mena
    Recuperació UF2 ASIXc 1B
    10/06/2022
    Ex.1

"""

def agafar_text():
    print("Que palabra?")
    palabra = input(" ")
    return palabra

def comptador():
    cadena = agafar_text()
    print("Que caracter?")
    caracter = (input(" "))
    contador_l = 0
    while caracter in cadena:
        contador_l += 1
        return print(contador_l)

comptador()
