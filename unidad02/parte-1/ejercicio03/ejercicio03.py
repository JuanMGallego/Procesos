import multiprocessing
from multiprocessing import Process, Queue
import time

# Método para leer los números del archivo
def leerNumeros(archivo, cola):

    with open(archivo, 'r') as file:
        for line in file:
            numero = int(line.strip())
            cola.put(numero)

    # Indicar el final de la lectura con None
    cola.put(None)

# Método para sumar los números del archivo
def sumarNumeros(cola, resultado):
    
    while True:
        numero = cola.get()
        if numero is None:
            break
        resultado.value += numero

if __name__ == "__main__":

    # Crear una cola para la comunicación
    cola = Queue()

    # Crear un objeto compartido para almacenar la suma total
    resultado = multiprocessing.Value("i", 0)

    # Definir el rango de números para cada proceso
    archivo = "ejercicio03/numeros.txt"

    # Medir el tiempo de inicio
    tiempoInicio = time.time()

    # Crear los procesos
    procesoLectura = Process(target=leerNumeros, args=(archivo, cola))
    procesoSuma = Process(target=sumarNumeros, args=(cola, resultado))

    # Iniciar los procesos
    procesoLectura.start()
    procesoSuma.start()

    # Esperar a que el proceso de lectura termine
    procesoLectura.join()

    # Esperar a que el proceso de suma termine
    cola.put(None)  # Indicar al proceso de suma que debe terminar
    procesoSuma.join()

    # Medir el tiempo de finalización
    tiempoFinal = time.time()

    # Imprimir la suma total
    print(f"La suma total de todos los números es: {resultado.value}")
    print(f"Tiempo de ejecución: {tiempoFinal - tiempoInicio} segundos")