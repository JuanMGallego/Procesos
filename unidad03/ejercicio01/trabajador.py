from random import randint
from threading import Thread
import time

class Trabajdor(Thread):
    def __init__(self, nombre):
        Thread.__init__(self)
        self.nombre = nombre

    def run(self):
        while(True):
            print("Soy ", self.nombre, " y estoy rabajando")
            time.sleep(randint(1, 10))
            print("Soy ", self.nombre, " y he trminado de trabajar")