import json

def leeFichero(nombreArchivo):
    data = []
    try:
        archivo = open(nombreArchivo, "r")
        data = json.load(archivo)
        archivo.close()
    except json.JSONDecodeError as e1:
        print("Error al cargar el archivo:", e1)
    except FileNotFoundError as e2:
        print("No se encuentra el archivo", e2)
    return data

def escribeFichero(nombreArchivo, data):
    archivo = open(nombreArchivo, "w")
    json.dump(data, archivo)
    archivo.close()

#Fución para generar un nuevo id mayor al máximo del listado buscado
def find_next_id(rutaArchivo):
    archivo = leeFichero(rutaArchivo)
    return max(elemento["id"] for elemento in archivo)+1