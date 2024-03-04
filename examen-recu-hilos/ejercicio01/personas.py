from threading import Condition, Thread
from random import randint
import time

# Clase persona
class Persona(Thread):

    colores = [False, False, False] #Amarillo, Magenta, cian (Booleanos para activar o desactivar y representar su uso)
    coloresNombre = ["AMARILLO", "MAGENTA", "CIAN"] # Lista con los nombres de los colores respectivamente

    # Utillizo condition ya que el fin del programa es que cada hilo solo pueda entrar en una sección crítica del código si
    # se cumple la condición de no estar siendo utilizada una posición del array, lo que representa un color primario.
    cond = Condition()

    # Constructor con parámetros
    def __init__(self, nombre, color1, color2, colorSec):
        Thread.__init__(self)
        self.nombre = nombre # Nombre de la persona (String)
        self.color1 = color1 # Posición del primer color primario en el array (Int)
        self.color2 = color2 # Posición del segundo color primario en el array (Int)
        self.colorSec = colorSec # Nombre del color secundario a conseguir (String)

    # Método Run que contiene el código que se va a ejecutar en cada hilo
    def run(self):

        # Bucle para estar haciéndose constantemente y que no paren de usar los colores
        while True:

            # Bloque que automáticamente realiza el acquire y release al principio y al final del mismo
            with Persona.cond:

                # Mientras estén ocupados los colores se quedará esperando
                while (Persona.colores[self.color1] or Persona.colores[self.color2]) == True:
                    print(f"{self.nombre} está esperando a que suelten sus colores")
                    Persona.cond.wait() # Espera a que sea notificado

                # Cuando ya ha entrado, bloquea los colores que va a usar
                Persona.colores[0] = True
                Persona.colores[1] = True

            # Representación por consola del uso de los colores
            print(f"{self.nombre} ha cogido el {Persona.coloresNombre[self.color1]} y el {Persona.coloresNombre[self.color2]}")
            print(f"{self.nombre} está pintando el color {self.colorSec}")
            time.sleep(randint(100, 500)/1000) # Pequeña espera para simular que está pintando
            print(f"{self.nombre} ha terminado con el {Persona.coloresNombre[self.color1]} y el {Persona.coloresNombre[self.color2]}")

            # Libera los colores y notifica a los demás hilos
            with Persona.cond:
                Persona.colores[0] = False
                Persona.colores[1] = False
                Persona.cond.notifyAll() # Notificación a los demás hilos
