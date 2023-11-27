from multiprocessing import Pool
import time

# Método para sumar los números del rango introducido por parámetro
def sumarNumeros(args):
    
    inicio, fin = args
    sumaParcial = sum(range(inicio, fin + 1))
    print(f"La suma de los números desde {inicio} hasta {fin} es: {sumaParcial}")
    return sumaParcial

if __name__ == "__main__":

    # Crear un Pool con el número deseado de procesos
    numProcesos = 4
    pool = Pool(processes=numProcesos)

    # Definir el rango de números para cada proceso
    rangos = [(1, 25), (26, 50), (51, 75), (76, 100)]

    # Medir el tiempo de inicio
    tiempoInicio = time.time()

    # Utilizar el Pool para realizar las sumas en paralelo
    resultadosParciales = pool.map(sumarNumeros, rangos)

    # Cerrar el Pool y esperar a que todos los procesos terminen
    pool.close()
    pool.join()

    # Calcular la suma total
    sumaTotal = sum(resultadosParciales)

    # Medir el tiempo de finalización
    tiempoFinal = time.time()

    # Imprimir la suma total y el tiempo de ejecución
    print(f"La suma total de todos los procesos es: {sumaTotal}")
    print(f"Tiempo de ejecución: {tiempoFinal - tiempoInicio} segundos")