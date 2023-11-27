import multiprocessing
import time

# Método para sumar los números del rango introducido por parámetro
def sumarRango(inicio, fin):

    resultado = sum(range(min(inicio, fin), max(inicio, fin) + 1))
    print(f"La suma de los números desde {min(inicio, fin)} hasta {max(inicio, fin)} es: {resultado}")

if __name__ == "__main__":

    # Definir los rangos de números para cada proceso
    rangos = [(1, 50), (51, 100), (100, 1)]

    # Medir el tiempo de inicio
    tiempoInicio = time.time()

    # Crear los procesos
    procesos = []

    for rango in rangos:
        proceso = multiprocessing.Process(target=sumarRango, args=rango)
        procesos.append(proceso)
        proceso.start()

    # Esperar a que todos los procesos terminen
    for proceso in procesos:
        proceso.join()

    # Medir el tiempo de finalización
    tiempoFinal = time.time()

    print("Todos los procesos han terminado.")
    print(f"Tiempo de ejecución: {tiempoFinal - tiempoInicio} segundos")