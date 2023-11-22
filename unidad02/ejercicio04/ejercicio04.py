import multiprocessing
from multiprocessing import Process, Pipe
import time

# Método para leer los números del archivo
def leerNumeros(archivo, pipe):

    with open(archivo, 'r') as file:
        for line in file:
            numero = int(line.strip())
            pipe.send(numero)
            
    # Indicar el final de la lectura con None
    pipe.send(None)

# Método para sumar los números del archivo
def sumarNumeros(pipe, resultado):

    while True:
        numero = pipe.recv()
        if numero is None:
            break
        resultado.value += numero

if __name__ == "__main__":
    
    # Crear una tubería para la comunicación
    pipeLectura, pipeSuma = Pipe()

    # Crear un objeto compartido para almacenar la suma total
    resultado = multiprocessing.Value("i", 0)

    # Definir el rango de números para cada proceso
    archivo = "numeros.txt"

    # Medir el tiempo de inicio
    tiempoInicio = time.time()

    # Crear los procesos
    procesoLectura = Process(target=leerNumeros, args=(archivo, pipeLectura))
    procesoSuma = Process(target=sumarNumeros, args=(pipeSuma, resultado))

    # Iniciar los procesos
    procesoLectura.start()
    procesoSuma.start()

    # Esperar a que el proceso de lectura termine
    procesoLectura.join()

    # Esperar a que el proceso de suma termine
    pipeSuma.send(None)  # Indicar al proceso de suma que debe terminar
    procesoSuma.join()

    # Medir el tiempo de finalización
    tiempoFinal = time.time()

    # Imprimir la suma total
    print(f"La suma total de todos los números es: {resultado.value}")
    print(f"Tiempo de ejecución: {tiempoFinal - tiempoInicio} segundos")