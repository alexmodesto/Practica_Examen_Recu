"""
    Àlex Modesto Mena
    Recuperació UF2 ASIXc 1B
    10/06/2022
    Ex.2
"""

def agafar_nombres():
    numeros = input(" ")
    return numeros


def ValorAPosicio(num):
    volta = 0
    posicio = []
    for i in num:
        posicio.append(volta)
        volta += 1
    return posicio

def mostrar_posicio():
    num = agafar_nombres()
    pos = ValorAPosicio(num)
    final = print(f"\nPosition: {pos}")
    return final

