import multiprocessing
import time

# Método para leer los números del archivo
def leerNumeros(archivo, cola):

    with open(archivo, 'r') as file:
        for line in file:
            numeros = tuple(map(int, line.strip().split()))
            cola.put(numeros)

    # Indicar el final de la lectura con None
    cola.put(None)

# Método para sumar todos los números de cada parte
def sumarPartes(cola, resultado):

    while True:
        numeros = cola.get()
        if numeros is None:
            break
        resultado.value += sum(numeros)

if __name__ == "__main__":

    # Crear una cola para la comunicación
    cola = multiprocessing.Queue()

    # Crear un objeto compartido para almacenar la suma total
    resultado = multiprocessing.Value("i", 0)

    # Definir el rango de números para cada proceso
    archivo = "ejercicio07/numeros.txt"

    # Medir el tiempo de inicio
    tiempoInicio = time.time()

    # Crear los procesos
    procesoLectura = multiprocessing.Process(target=leerNumeros, args=(archivo, cola))
    procesoSuma = multiprocessing.Process(target=sumarPartes, args=(cola, resultado))

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
    print(f"La suma total de los pares de números es: {resultado.value}")
    print("Todos los procesos han terminado.")
    print(f"Tiempo de ejecución: {tiempoFinal - tiempoInicio} segundos")