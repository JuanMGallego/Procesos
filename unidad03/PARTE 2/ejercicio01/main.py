from adivinador import *

if __name__ == "__main__":
    lista = []
    for i in range(20):
        hilo = Adivinador(("hilo", i))
        hilo.start()
        lista.append(hilo)

    for h in lista:
        h.join()