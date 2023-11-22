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

    # Crear un Pool con el número deseado de procesos
    numProcesos = 3
    with multiprocessing.Pool(processes=numProcesos) as pool:
        # Utilizar el Pool para realizar las sumas en paralelo
        pool.starmap(sumarRango, rangos)

    # Medir el tiempo de finalización
    tiempoFinal = time.time()

    print("Todos los procesos han terminado.")
    print(f"Tiempo de ejecución: {tiempoFinal - tiempoInicio} segundos")