# Crea un proceso que cuente las vocales de un fichero de texto.
# Para ello crea una función que reciba una vocal y devuelva cuántas veces aparece en un fichero.
# Lanza el proceso de forma paralela para las 5 vocales.
# Tras lanzarse se imprimirá el resultado por pantalla.

from multiprocessing import Process, Queue

archivo = "ejercicio01/vocales.txt"

def contarVocal(vocal):

    contador = 0
    lector = open(archivo, 'r')

    for caracter in lector:
        if (caracter == vocal):
            contador = contador + 1
    
    lector.close

    return contador

if __name__ == '__main__':

    vocales = ['a', 'e', 'i', 'o', 'u']

    for vocal in vocales:
        p = Process(target=contarVocal, args=(vocal))