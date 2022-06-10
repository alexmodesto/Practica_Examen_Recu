"""

  Javier Amaya Boira / José Luis Álvarez Casas

   01/03/2022

   ASIXc M03 UF2 A1 Disseny Descendent

   Exeemple: Menu amb Opcions

"""

# Mètodes

# -----------------------------------------------------------------------------

from datetime import date

from datetime import datetime

from time import sleep

# Mostra en pantalla el menú d'opcions i # demana per teclat quina es vol.

# La funció retorna el valor de l'opció triada.

def obteOpcio():

  print("1.- Primera opció")

  print("2.- Millor opció")

  print("3.- Jo triaria aquesta")

  print("4.- La millor opció")

  print("5.- Sortir")

  return int(input())

def opcioPrimera():

  print("Primera opció")

  sleep(2)

def opcioMillor():

  print("Millor opció")

  sleep(2)

def opcioJoTriariaAquesta():

  print("Jo triaria aquesta")

  sleep(2)

def opcioLaMillor():

  print("La millor opció")

  sleep(2)

def tractarError(missatge):

  # Obtenir la data del sistema i l'hora

  avui = date.today()

  ara = datetime.now()



  # Formatar la data i l'hora

  # Textual month, day and year

  avui = avui.strftime("%B %d, %Y")

  # dd/mm/YY H:M:S

  ara = ara.strftime("%d/%m/%Y %H:%M:%S")

  """

  # dd/mm/YY

  avui = avui.strftime("%d/%m/%Y")

  # mm/dd/y

  avui = avui.strftime("%m/%d/%y")

  # Month abbreviation, day and year

  avui = avui.strftime("%b-%d-%Y")

  """

  # Mostrar missatge

  print("========================")

  print(f"{avui}\n{ara}\nERROR: {missatge}")

  print("========================")

def tractamentFinal():

  for i in range (5):

     print(".",end="")

     sleep(1)

  print("See you")



# Programa principal

# -----------------------------------------------------------------------------

# Mostrem el menú i demanem quina opció es vol executar

opcio = obteOpcio()

# Mentre no ens demanin sortir, atenem a l'opció triada

while opcio != 5:

  if opcio < 1 or opcio > 4:

     tractarError("opció no valida")

  else:

     if opcio == 1:

        opcioPrimera()

     elif opcio == 2:

        opcioMillor()

     elif opcio == 3:

        opcioJoTriariaAquesta()

     elif opcio == 4:

        opcioLaMillor()

  # tornem a presentar el menú i a llegir l'opció triada

  opcio = obteOpcio()

# Tractament final

tractamentFinal()