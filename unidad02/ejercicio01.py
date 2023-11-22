import multiprocessing
import time

# Método para sumar los números del rango introducido por parámetro
def sumarNumeros(inicio, fin):
    
    resultado = sum(range(inicio, fin + 1))
    print(f"La suma de los números desde {inicio} hasta {fin} es: {resultado}")

if __name__ == "__main__":

    # Definir el rango de números para cada proceso
    rangoProceso1 = (1, 50)
    rangoProceso2 = (51, 100)

    # Medir el tiempo de inicio
    tiempoInicio = time.time()

    # Crear los procesos
    proceso1 = multiprocessing.Process(target=sumarNumeros, args=rangoProceso1)
    proceso2 = multiprocessing.Process(target=sumarNumeros, args=rangoProceso2)

    # Iniciar los procesos
    proceso1.start()
    proceso2.start()

    # Esperar a que todos los procesos terminen
    proceso1.join()
    proceso2.join()

    # Medir el tiempo de finalización
    tiempoFinal = time.time()

    # Mostrar el tiempo de ejecución
    print("Todos los procesos han terminado.")
    print(f"Tiempo de ejecución: {tiempoFinal - tiempoInicio} segundos")