"""

    Àlex Modesto Mena-Iker Mera Murillo
    ASIXc 1B UF1 (Recuperació)

"""
import random

def demanarFrase():
    frase_demanada = (input("").split())
    return frase_demanada
frase = []
frase_desordenada = []

def mezcla_letras_palabra(frase_demanada): #Aquesta funció barreja les lletres de les paraules
    palabra_desordenada = []
    for palabra in frase_demanada:
        lista1 = []
        if len(palabra) > 3:
            primera_lletra = palabra[0]
            ultima_lletra = palabra[-1]
            mig = palabra[1:-1]
            for i in mig:
                lista1.append(i)
            random.shuffle(lista1)
            palabra_desordenada.extend(primera_lletra)
            palabra_desordenada.extend(lista1)
            palabra_desordenada.extend(ultima_lletra)
            frase_desordenada.append(palabra_desordenada)
            lista1 = []
            palabra_desordenada = []
        else:
            frase_desordenada.append(palabra)

    return palabra_desordenada

def montar_frase():
    result = " "
    for paraula in frase_desordenada:
       for letra in paraula:
           result += letra
       result += " "
    return result

def ParaulesBoges(): #Aquesta funció junta les funcion del crazy words per a poder utilitzarles comodament en el main
    demanar_frase = demanarFrase()
    mezcla_letras_palabra(demanar_frase)
    return montar_frase()

resultat = ParaulesBoges()

print (resultat)