import json

def leerFichero(rutaFichero):
        archivo = open(rutaFichero, "r")
        data = json.load(archivo)
        archivo.close()
        return data

def find_next_id(rutaFichero):
        archivo = open(rutaFichero, "r")
        return max(archivo["id"] for marca in archivo) + 1