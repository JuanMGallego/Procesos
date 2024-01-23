from cliente import *

if __name__ == "__main__":
    lista = []
    for i in range(20):
        hilo = Cliente(str(i))
        hilo.start()
        lista.append(hilo)

    for h in lista:
        h.join()