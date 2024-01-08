from threading import Thread

class Raton(Thread):
    def __init__(self, nombre, tiempoAlimentacion):
        Thread.__init__(self)
        self.nombre = nombre
        self.tiempoAlimentacion = tiempoAlimentacion

    def run(self):
        print("El ratón", self.nombre, "ha empezado a comer")
        
        return super().run()