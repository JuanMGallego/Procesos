from estudiante import *

lista = []
for i in range(4):
    hilo = Estudiante(str(i))
    hilo.start()
    lista.append(hilo)

for h in lista:
    h.join()