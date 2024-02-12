from threading import Thread, Semaphore
from random import randint
import time

class Cliente(Thread):
    sDependiente = Semaphore(5)
    sTicket = Semaphore(2)

    def __init__(self, nombre):
        Thread.__init__(self, name = nombre)

    def run(self):

        time.sleep(randint(1, 5))

        print(f"El cliente {self.name} se ha puesto en la cola de tickets")

        with Cliente.sTicket:
            print(f"El cliente {self.name} está usando la máquina de tickets.")
            time.sleep(randint(1,4))
            print(f"El cliente {self.name} ha sacado el ticket.")
        
        print(f"El cliente {self.name} se ha puesto en la cola del mostrador")

        with Cliente.sDependiente:
            print(f"El cliente {self.name} está siendo atendido por un dependiente.")
            time.sleep(randint(3,7))
            print(f"El cliente {self.name} ha terminado de ser atendido.")
