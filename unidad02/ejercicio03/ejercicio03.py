import multiprocessing
import time

def leer_numeros(nombre_archivo, cola):
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            numero = int(linea.strip())
            cola.put(numero)

def suma_hasta_n_con_colas(cola, result_queue):
    suma = 0
    while not cola.empty():
        numero = cola.get()
        suma += numero
    result_queue.put(suma)

if __name__ == "__main__":
    # Nombre del archivo que contiene los números (uno por línea)
    nombre_archivo = "numeros.txt"

    # Crear una cola para compartir los números entre los procesos
    cola_numeros = multiprocessing.Queue()

    # Lanzar un proceso para leer los números del archivo y colocarlos en la cola
    proceso_lectura = multiprocessing.Process(target=leer_numeros, args=(nombre_archivo, cola_numeros))
    proceso_lectura.start()
    proceso_lectura.join()  # Esperar a que termine el proceso de lectura

    # Lanzar un proceso para calcular la suma utilizando los números de la cola
    result_queue = multiprocessing.Queue()
    proceso_suma = multiprocessing.Process(target=suma_hasta_n_con_colas, args=(cola_numeros, result_queue))

    # Medir el tiempo de inicio
    start_time = time.time()

    # Iniciar el proceso de suma
    proceso_suma.start()
    proceso_suma.join()  # Esperar a que termine el proceso de suma

    # Obtener el resultado de la cola
    suma_total = result_queue.get()

    # Medir el tiempo de finalización
    end_time = time.time()

    # Imprimir el resultado y el tiempo de ejecución
    print(f"La suma de los números leídos del archivo es: {suma_total}")
    print(f"Tiempo de ejecución: {end_time - start_time} segundos")