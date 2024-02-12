from threading import Barrier
from participante import *

barrera = Barrier(10)
lista = []

for i in range(10):
    hilo = Participante(str(i), barrera)
    hilo.start()
    lista.append(hilo)

for h in lista:
    h.join()