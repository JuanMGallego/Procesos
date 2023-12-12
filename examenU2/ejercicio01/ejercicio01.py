from multiprocessing import Pool
import random

#Proceso que recibe el dia y crea los archivos con sus tems aleatorias
def proceso1(dia):

    #Modificador si necesita 0 delane
    nombreFichero = f"{dia}-12"

    if dia < 10:
        nombreFichero = f"0{dia}-12"

    #Escribe en el archivo
    with open(f"ejercicio01/{nombreFichero}.txt", "w") as archivo:

        for _ in range(1, 25):
            archivo.write(f"{round(random.uniform(0, 20), 2)}\n")

#Proceso que recive el dia y crea otro con la temp maxima
def proceso2(dia):

    nombreFichero = f"{dia}-12"

    if dia < 10:
        nombreFichero = f"0{dia}-12"

    temps = []

    with open(f"ejercicio01/{nombreFichero}.txt", "r") as archivoTemps:
        temps = [line.strip() for line in archivoTemps]

    with open("ejercicio01/maximas.txt", "w") as archivoMaximas:
        archivoMaximas.write(f"{nombreFichero}:{max(temps)}\n")

#Proceso que recive el dia y crea otro con la temp minima
def proceso3(dia):

    nombreFichero = f"{dia}-12"

    if dia < 10:
        nombreFichero = f"0{dia}-12"

    with open(f"ejercicio01/{nombreFichero}.txt", "r") as archivoTemps:
        temps = [line.strip() for line in archivoTemps]

    with open("ejercicio01/minimas.txt", "w") as archivoMinimas:
        archivoMinimas.write(f"{nombreFichero}:{min(temps)}\n")

#Main con todas los procesos
if __name__ == "__main__":

    with Pool(processes=31) as pool:
        pool.map(proceso1, range(1, 32))

    with Pool(processes=31) as pool:
        pool.map(proceso2, range(1, 32))
        pool.map(proceso3, range(1, 32))
        
