import random
from multiprocessing import Pool

# Proceso 1
def generar_notas(numero_alumno):
    notas = [round(random.uniform(1, 10), 2) for _ in range(6)]
    ruta_fichero = f"Alumno{numero_alumno}.txt"

    with open(ruta_fichero, 'w') as file:
        for nota in notas:
            file.write(f"{nota}\n")

# Proceso 2
def calcular_media_y_guardar(numero_alumno):
    ruta_notas = f"Alumno{numero_alumno}.txt"
    nombre_alumno = f"Alumno{numero_alumno}"
    
    with open(ruta_notas, 'r') as file:
        notas = [float(line.strip()) for line in file]

    media = sum(notas) / len(notas)

    with open("medias.txt", 'a') as file:
        file.write(f"{media} {nombre_alumno}\n")

# Proceso 3
def encontrar_nota_maxima():
    with open("medias.txt", 'r') as file:
        lineas = file.readlines()

    if not lineas:
        print("No hay datos en el archivo de medias.")
        return

    max_linea = max(lineas, key=lambda x: float(x.split()[0]))
    nota_maxima, nombre_alumno = map(float, max_linea.split())
    
    print(f"Nota máxima: {nota_maxima}, Alumno: {nombre_alumno}")

if __name__ == "__main__":
    # Proceso 1
    with Pool() as pool:
        pool.map(generar_notas, range(1, 11))

    # Proceso 2
    with Pool() as pool:
        pool.map(calcular_media_y_guardar, range(1, 11))

    # Proceso 3
    encontrar_nota_maxima()