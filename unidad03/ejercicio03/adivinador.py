from threading import Thread
from random import randint

class Adivinador(Thread):

    numero_secreto = randint(0, 100)
    acertado = False

    def __init__(self, nombre):
        Thread.__init__(self)
        self.nombre = nombre

    def run(self):

        numero_aleatorio = 0

        while (Adivinador.acertado == False):
            numero_aleatorio = randint(0, 100)
            
            if (numero_aleatorio == Adivinador.numero_secreto):
                Adivinador.acertado = True
                print("El ", self.nombre, " ha acertado el numero secreto sacando un ", numero_aleatorio, "\nEl numero oculto es: ", Adivinador.numero_secreto)
