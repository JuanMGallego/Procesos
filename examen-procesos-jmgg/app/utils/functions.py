import json

def leeFichero(nombreArchivo):
    archivo = open(nombreArchivo, "r")
    data = json.load(archivo)
    archivo.close()
    return data

def escribeFichero(nombreArchivo, data):
    archivo = open(nombreArchivo, "w")
    json.dump(data, archivo)
    archivo.close()

#Buscar id una a una
def find_next_id(fichero):
    departamentos = leeFichero(fichero)
    max = departamentos[0]["id"]
    for departamento in departamentos:
        if departamento["id"] > max:
            max = departamento["id"]

    return max+1