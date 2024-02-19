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
