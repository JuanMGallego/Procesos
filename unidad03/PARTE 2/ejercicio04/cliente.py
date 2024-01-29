from threading import Thread, Semaphore
from random import randint
import time

class Cliente(Thread):
    sCarn = Semaphore(4)
    sChar = Semaphore(2)

    def __init__(self, nombre):
        Thread.__init__(self, name = nombre)

    def run(self):
        atendidoCarn = False
        atendidoChar = False

        print("El cliente", self.name, "se ha puesto en la cola.")

        while(not atendidoCarn or not atendidoChar):

            if(Cliente.sCarn._value > 0 and not atendidoCarn):
                with Cliente.sCarn:
                    atendidoCarn = True
                    print("El cliente", self.name, "esta siendo atendido en la carniceria.")
                    time.sleep(randint(1, 10))

                    print("El cliente", self.name, "ha terminado en la carniceria.")

            if(Cliente.sCarn._value > 0 and not atendidoChar):
                with Cliente.sChar:
                    atendidoChar = True
                    print("El cliente", self.name, "esta siendo atendido en la charcuteria.")
                    time.sleep(randint(1, 10))

                    print("El cliente", self.name, "ha terminado en la charcuteria.")

        print("El cliente", self.name, "se ha terminado de comprar.")
            
            

        