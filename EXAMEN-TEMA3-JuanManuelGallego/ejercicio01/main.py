from cliente import *

lista = []

for i in range(10):
    hilo = Cliente(str(i))
    hilo.start()
    lista.append(hilo)

for h in lista:
    h.join()