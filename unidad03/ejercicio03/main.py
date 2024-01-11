from adivinador import *

hilos = [Adivinador("Hilo " + str(_)) for _ in range(10)]

for a in hilos:
    a.start()

for a in hilos:
    a.join()