from threading import Thread, Semaphore
from random import randint
import time

class Cliente(Thread):
    s = Semaphore(4)

    def __init__(self, nombre):
        Thread.__init__(self, name = nombre)

    def run(self):

        print("El cliente", self.name, "se ha puesto en la cola.")

        Cliente.s.acquire()
        print("El cliente", self.name, "esta siendo atendido.")
        time.sleep(randint(1, 10))

        Cliente.s.release()
        print("El cliente", self.name, "ha terminado en la carniceria.")