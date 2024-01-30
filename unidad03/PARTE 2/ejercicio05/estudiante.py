from threading import Condition, Thread
from random import randint
import time

class Estudiante(Thread):

    libros = [False, False, False, False, False, False, False, False, False]
    cond = Condition()

    def __init__(self, nombre):
        Thread.__init__(self, name = nombre)

    def run(self):
        libro1 = Estudiante.libros[randint(0, 8)]
        libro2 = Estudiante.libros[randint(0, 8)]

        while(libro1 == libro2):
            libro2 = Estudiante.libros[randint(0, 8)]
            
        print("El estudiante", self.name, "ha elegido sus dos libros")

        Estudiante.cond.acquire()
        while (Estudiante.libros[libro1] == True and Estudiante.libros[libro2] == True):
            print("El estudiante", self.name, "está esperando a que dejen los libros que quiere")
            Estudiante.cond.wait()

        Estudiante.libros[libro1] = True
        Estudiante.libros[libro2] = True

        Estudiante.cond.release()

        print("El estudiante", self.name, "está usando los libros")
        time.sleep(randint(3, 5))
        print("El estudiante", self.name, "ha terminado con los libros")

        Estudiante.cond.acquire()
        Estudiante.libros[libro1] = False
        Estudiante.libros[libro2] = False
        Estudiante.cond.notifyAll()
        Estudiante.cond.release