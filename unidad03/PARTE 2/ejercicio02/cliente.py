from threading import Thread, Lock
from random import randint
import time

class Cliente(Thread):

    numero_secreto = randint(0, 100)
    acertado = False
    l = Lock()

    def __init__(self, nombre):
        Thread.__init__(self, name = nombre)

    def run(self):

        print("El cliente", self.name, "se ha puesto en la cola.")

        Cliente.l.acquire()
        print("El cliente", self.name, "esta siendo atendido.")
        time.sleep(1, 5)

        print("El cliente", self.name, "se ha marchado.")
        Cliente.l.release()
