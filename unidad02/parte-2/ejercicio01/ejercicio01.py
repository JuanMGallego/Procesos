from multiprocessing import Pool

# Archivo con el texto a analizar
archivo = "ejercicio01/vocales.txt"

# Método para leer el archivo y devolver sus vocales
def contarVocales(vocal):
    with open(archivo, "r") as file:
        contenido = file.read()
        cont = contenido.count(vocal)
    return cont

# Main que llama al archivo por cada vocal
if __name__ == "__main__":

    # Array con las vocales por las que filtrar
    vocales = ['a', 'e', 'i', 'o', 'u']

    # Se usa pool para lanzar varios procesos para dar valores distintos por cada vocal
    with Pool(len(vocales)) as pool:
        resultados = pool.map(contarVocales, vocales)

    # Bucle para mostrar una linea con el resultado de cada vocal
    for vocal, veces in zip(vocales, resultados):
        print(f"La vocal {vocal} aparece {veces} veces en el archivo.")