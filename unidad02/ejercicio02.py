import multiprocessing
import time

def sumarHastaNParcial(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma

if __name__ == "__main__":

    valor = int(input("Introduce un valor: "))

    # Cambia el número de procesos según sea necesario
    numProcesos = 4

    # Medir el tiempo de inicio
    tiempoInicio = time.time()

    with multiprocessing.Pool(processes=numProcesos) as pool:

        # Divide el rango de números en partes iguales para cada proceso
        partes = [valor // numProcesos] * numProcesos
        
        # El último proceso se encarga de los posibles restos
        partes[-1] += valor % numProcesos

        # Calcula la suma de cada parte
        resultParcial = pool.map(sumarHastaNParcial, partes)

    # Combina los resultados parciales para obtener la suma total
    sumaTotal = sum(resultParcial)

    # Medir el tiempo de finalización
    tiempoFinal = time.time()

    # Imprimir el resultado y el tiempo de ejecución
    print(f"La suma de los números del 1 al {valor} es: {sumaTotal}")
    print(f"Tiempo de ejecución: {tiempoFinal - tiempoInicio} segundos")