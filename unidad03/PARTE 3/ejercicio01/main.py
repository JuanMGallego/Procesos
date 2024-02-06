from participante import *

lista = []
for i in range(10):
    hilo = Participante(str(i))
    hilo.start()
    lista.append(hilo)

for h in lista:
    h.join()