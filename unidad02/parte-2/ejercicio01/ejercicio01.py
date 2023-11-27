import multiprocessing
import time

# Método para leer el archivo y contar cada vocal
def contarVocal(vocal, archivo, resultadoCola):
    with open(archivo, 'r') as archivo:
        contenido = archivo.read()
        contador = contenido.lower().count(vocal)
        resultadoCola.put((vocal, contador))

if __name__ == "__main__":
    # Nombre del archivo que contiene el texto
    archivo = "ejercicio01/vocales.txt"

    # Lista de vocales
    vocales = ['a', 'e', 'i', 'o', 'u']

    # Crear una cola para compartir los resultados entre procesos
    resultadoCola = multiprocessing.Queue()

    # Crear procesos para contar las vocales de forma paralela
    procesos = [multiprocessing.Process(target=contarVocal, args=(vocal, archivo, resultadoCola)) for vocal in vocales]

     # Medir el tiempo de inicio
    tiempoInicio = time.time()

    # Iniciar los procesos
    for proceso in procesos:
        proceso.start()

    # Esperar a que todos los procesos terminen
    for proceso in procesos:
        proceso.join()

    # Obtener los resultados de la cola
    resultados = []
    while not resultadoCola.empty():
        resultados.append(resultadoCola.get())

    # Medir el tiempo de finalización
    tiempoFinal = time.time()

    # Imprimir los resultados por pantalla
    for vocal, contador in resultados:
        print(f"La vocal '{vocal}' aparece {contador} veces en el archivo.")

    print(f"Tiempo de ejecución: {tiempoFinal - tiempoInicio} segundos")