from threading import Condition, Thread
from random import randint
import time

total = 0
MAX_DINERO = 2000

cond = Condition()

class Voluntario(Thread):

    def __init__(self, nombre):
        Thread.__init__(self, name = nombre)

    def run(self):

        global total
        global MAX_DINERO

        while (True):

            #Variable se inicializa dentro del while para resetearla cada iteración.
            recaudado = 0

            #Inicio de la recolección.
            print(f"El voluntario {self.name} está recolectando")
            time.sleep(randint(1,3))
            recaudado = randint(4, 25)
            print(f"El voluntario {self.name} ha recaudado {recaudado}€")

            with cond:
                if (MAX_DINERO - total <= recaudado):
                    print(f"El voluntario {self.name} está esperando para meter el dinero")
                    print(f"TOTAL: {total}")
                    cond.wait()

                #Se le suma lo recaudado por el voluntario al dinero total
                total += recaudado
                print(f"El voluntario {self.name} ha metido el dinero")
                print(f"TOTAL: {total}")


class Gestor(Thread):

    def __init__(self, nombre):
        Thread.__init__(self, name = nombre)

    def run(self):

        global total
        global MAX_DINERO

        while (True):

            #Variable se inicializa dentro del while para resetearla cada iteración.
            cogido = 0

            #Inicio de la recolección
            print(f"El gestor {self.name} está pensando cuanto dinero coger")
            time.sleep(randint(2,5))
            cogido = randint(10, 40)
            print(f"El gestor {self.name} quiere coger {cogido}€")

            with cond:
                if (total < cogido):
                    print(f"El gestor {self.name} está esperando para coger el dinero")
                    print(f"TOTAL: {total}")
                    cond.wait()

                #Se le resta lo cogido por el gestor al dinero total
                total -= cogido
                print(f"El gestor {self.name} ha cogido el dinero")
                print(f"TOTAL: {total}")
