import multiprocessing
import time

def sumaHastaN(n, resultadoCola):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    resultadoCola.put(suma)

if __name__ == "__main__":

    valor = int(input("Introduce un valor: "))

    # Crear una cola para obtener el resultado de cada proceso
    resultadoCola = multiprocessing.Queue()

    # Crear dos procesos para dividir el trabajo
    process1 = multiprocessing.Process(target=sumaHastaN, args=(valor // 2, resultadoCola))
    process2 = multiprocessing.Process(target=sumaHastaN, args=(valor, resultadoCola))

    # Medir el tiempo de inicio
    tiempoInicio = time.time()

    # Iniciar los procesos
    process1.start()
    process2.start()

    # Esperar a que ambos procesos terminen
    process1.join()
    process2.join()

    # Obtener los resultados de la cola
    sumaTotal = resultadoCola.get() + resultadoCola.get()

    # Medir el tiempo de finalización
    tiempoFinal = time.time()

    # Imprimir el resultado y el tiempo de ejecución
    print(f"La suma de los números del 1 al {valor} es: {sumaTotal}")
    print(f"Tiempo de ejecución: {tiempoFinal - tiempoInicio} segundos")