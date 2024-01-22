from threading import Thread

class Contador(Thread):
    archivo = "ejercicio04/vocales.txt"

    def __init__(self, vocal):
        Thread.__init__(self)
        self.vocal = vocal

    def run(self):

        contador = 0

        lector = open(Contador.archivo, 'r')

        for caracter in lector:
            if (caracter == self.vocal):
                contador =+ 1
    
        lector.close

        print(f"La vocal {self.vocal} aparece {contador} veces.")