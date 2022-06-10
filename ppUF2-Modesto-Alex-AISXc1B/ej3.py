"""
    Àlex Modesto Mena
    Recuperació UF2 ASIXc 1B
    10/06/2022
    Ex.2
"""


columna = int(input("\nIntrodueix el número de columnes (en NUMEROS!!!): "))
fila = int(input("Introdueix el número de files (en NUMEROS!!!): "))

while columna != fila or columna % 2 == 0 and fila % 2 == 0:
    print("\nEl número de files i columnes ha ser el mateix!!")
    columna = int(input("\nIntrodueix el número de columnes (en NUMEROS!!!): "))
    fila = int(input("Introdueix el número de files (en NUMEROS!!!): "))

print("Aqui tens la teva taula!!")
print()
for y in range(columna):
    for x in range(fila):
        if y == 0 or y == columna -1:
            print(" 1 ", end="")
        elif x == 0 or x == fila - 1:
            print(" 1 ", end="")
        else:
            print(" 0 ", end="")

    print("")

print("\nPROGRAMA FINALITZAT")
