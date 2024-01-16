from utils.functions import *
from flask import Blueprint, jsonify, request

rutaMarcas = "app/ficheros/marcas.json"

marcasBP = Blueprint("marcas", rutaMarcas)

@marcasBP.get("/")
def get_marcas():
    marcas = leerFichero(rutaMarcas)
    return jsonify(marcas)

@marcasBP.get("/<int:id>")
def get_marca(id):
    marcas = leerFichero(rutaMarcas)

    for marca in marcas:
        if marca["id"] == id:
            return jsonify(marca), 200
    return {"error":"Marca no encontrada"}, 404

@marcasBP.post("/")
def add_marca():
    marcas = leerFichero(rutaMarcas)

    if request.is_json:
        newMarca = request.get_json()
        newMarca["id"] = find_next_id(rutaMarcas)
        marcas.append(newMarca)