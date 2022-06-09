"""
 Ex2
"""
def agafar_nom():
    agafar=input('Quin és el teu nom? ')
    return agafar

def calcular_lletes(nom):
    """Esta funcion calcula la cantidad de veces que se encuentra un caracter identico"""
    vegadas_trobada = []
    lletras = []
    for i in nom:
        if i not in lletras:
            lletras.append(i)
            vegadas_trobada.append(1)
        else:
            a = lletras.index(i)
            vegadas_trobada[a] += 1
    return vegadas_trobada

#TODO: Añadir la posicion seguidas si se trata de la misma letra
def calcular_posicio(nom):
    """Esta funcion calcula la posicoon de cada caracter"""
    volta = 0
    posicio = []
    for i in nom:
        posicio.append(volta)
        volta += 1
    return posicio
#def mostrar_resultat(vegadestrobades,posicio,nom):


#TODO: Printa com formatat com demana el exercici

def mostrar_posicion_veces():
    """Esta funcion devuelve el caracter + la posicon + veces"""
    nom = agafar_nom()
    pos = calcular_posicio(nom)
    cal = calcular_lletes(nom)
    resultat = 'Letras Quantitat Posicio'
    final = print(f'\nLletra: {nom}\n Quantitat{cal}\n Posicio:{pos}')
    return final
#mostrar_resultat(a,c,d)
