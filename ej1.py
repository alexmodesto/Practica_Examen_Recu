"""
Ex1
"""
def agafar_text():
    recoger =input("")
    return recoger
vocales_accentuadas = ['á','à','é','è','í','ì','ó','ò','ú','ù']

def comptar_lletres():
    """Este programa cuenta los caracteres q se encuentran en una frase/nombre"""
    cadena = agafar_text()
    contador_l = 0
    #TODO: Implementar que compti les lletres amb signes d'accetuació
    for lletras in cadena:
        if (ord(lletras) >=65 and ord(lletras) <=90) or lletras in vocales_accentuadas:
            contador_l += 1
        elif ord(lletras) >= 97 and ord(lletras) <=122:
            contador_l +=1
    return print(contador_l)

