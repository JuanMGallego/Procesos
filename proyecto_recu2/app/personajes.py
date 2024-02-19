from functions import *
from flask_jwt_extended import jwt_required
from flask import Blueprint, jsonify, request

rutaComics = "ficheros/comics.json"
rutaPersonajes = "ficheros/personajes.json"

personajesBP = Blueprint("personajes", __name__)

@personajesBP.get("/<int:id_personaje>")
def get_personaje(id_personaje):
    personajes = leeFichero(rutaPersonajes)
    print(personajes)

    for personaje in personajes:
        if personaje["id_personaje"] == id_personaje:
            return personaje, 200
        
    return {"error":"Personaje no encontrado"}, 404

@personajesBP.patch("/<int:id_personaje>")
def modify_personaje(id_personaje):
    personajes = leeFichero(rutaPersonajes)

    if request.is_json:
        # variable para almacenar el json que llega
        newPersonaje = request.get_json()
        # Se busca por el id el personaje
        for personaje in personajes:
            if personaje["id_personaje"] == id_personaje:
                # Se modifican todos los atributos del personaje por los nuevos
                for element in newPersonaje:
                    if element == newPersonaje["tipo"] or element == newPersonaje["afiliacion"]:
                        personaje[element] = newPersonaje[element]
                escribeFichero(rutaPersonajes, personaje)
                # se devuelve el personaje junto al código de exito
                return personaje, 200
        # Si no se encuentra el personaje se devuelve un error y el codigo 404
        return {"error": "Personaje no encontrado"}, 404
    # Si no es json se devuelve un error y el codigo 415
    return {"error": "Request must be JSON"}, 415