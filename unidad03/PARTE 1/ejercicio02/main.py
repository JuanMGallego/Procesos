from contador import *

hilos = [Contador() for _ in range(10)]

for c in hilos:
    c.start()

for c in hilos:
    c.join()