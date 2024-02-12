from random import randint
from threading import Barrier, Thread
import time

class Participante(Thread):

    def __init__(self, nombre, barrera: Barrier):
        Thread.__init__(self, name = nombre)
        self.barrera = barrera

    def run(self):
        print(f"El participante {self.name} se ha puesto en la linea de salida")
        self.barrera.wait()
        time.sleep(3)
        print(f"El participante {self.name} sale de la línea de salida")
        startTime = time.time()
        time.sleep(randint(1,10))
        fisnishTime = time.time()
        print(f"El participante {self.name} ha terminado con un tiempo de {round(fisnishTime - startTime, 4)} segundos")
        