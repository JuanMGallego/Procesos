from personas import *

# Creación de los hilos con sus propiedades
persona1 = Persona("Pedro", 0, 1, "ROJO")
persona2 = Persona("Juanma", 1, 2, "AZUL")
persona3 = Persona("Javi", 0, 2, "VERDE")

# Se inician los hilos
persona1.start()
persona2.start()
persona3.start()

# se espera a que terminen los hilos para terminar el principal
persona1.join()
persona2.join()
persona3.join()