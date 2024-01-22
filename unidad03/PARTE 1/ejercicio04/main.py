from contador import *

vocales = ['a', 'e', 'i', 'o', 'u']

hilos = [Contador(vocal) for vocal in vocales]

for hilo in hilos:
    hilo.start()

for hilo in hilos:
    hilo.join()