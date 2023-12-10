import multiprocessing

def proceso1(archivo, año, cola):
    with open(archivo, 'r') as file:
        for linea in file:
            nombre, anoEstreno = linea.strip().split(';')
            if int(anoEstreno) == año:
                cola.put((nombre, anoEstreno))

def proceso2(cola):
    while True:
        pelicula = cola.get()
        if pelicula is None:
            break

        nombre, anoEstreno = pelicula
        nombre_fichero = f"peliculas{anoEstreno}.txt"
        with open(nombre_fichero, 'a') as file:
            file.write(f"{nombre};{anoEstreno}\n")

if __name__ == "__main__":

    año = int(input("Introduce un año (menor al actual): "))
    archivo = input("Introduce la ruta del fichero de películas: ")

    # Controlar que el año sea menor
    if año >= 2023:
        print("El año debe ser menor al actual.")
        exit()

    cola = multiprocessing.Queue()

    # Proceso 1
    proceso1 = multiprocessing.Process(target=proceso1, args=(archivo, año, cola))
    proceso1.start()

    # Proceso 2
    proceso2 = multiprocessing.Process(target=proceso2, args=(cola,))
    proceso2.start()

    # Esperar a que el Proceso 1 termine
    proceso1.join()

    # Indicar al Proceso 2 que no hay más datos
    cola.put(None)
    
    # Esperar a que el Proceso 2 termine
    proceso2.join()

    print(f"Proceso completado. Las películas del año {año} se han almacenado en ficheros correspondientes.")