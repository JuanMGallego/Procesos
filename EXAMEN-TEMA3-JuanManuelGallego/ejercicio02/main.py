from personas import *


#Iguales se ejecutan siempre porque estan igualados, si no hay que ponerle más a los voluntarios para que llege al maximo y al revés.
VOLUNTARIOS = 4
GESTORES = 4

listaVol = []
listaGes = []

for i in range(VOLUNTARIOS):
    hilo = Voluntario(str(i))
    hilo.start()
    listaVol.append(hilo)

for i in range(GESTORES):
    hilo = Gestor(str(i))
    hilo.start()
    listaGes.append(hilo)

