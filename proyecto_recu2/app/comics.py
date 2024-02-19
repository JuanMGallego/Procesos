from functions import *
from flask_jwt_extended import jwt_required
from flask import Blueprint, jsonify, request

rutaComics = "ficheros/comics.json"
rutaPersonajes = "ficheros/personajes.json"

comicsBP = Blueprint("comics", __name__)

@comicsBP.get("/<int:id_comic>/<string:tipo>/<int:id_personaje>")
def get_comic_personaje(id_comic, tipo, id_personaje):
    personajes = leeFichero(rutaPersonajes)

    if tipo == "heroes":
        for personaje in personajes:
            if personaje["id_comic"] == id_comic and personaje["tipo"] == "Heroe" and personaje["id_personaje"] == id_personaje:
                return jsonify(personaje), 200
            
    elif tipo == "villanos":
        for personaje in personajes:
            if personaje["id_comic"] == id_comic and personaje["tipo"] == "Villano" and personaje["id_personaje"] == id_personaje:
                return jsonify(personaje), 200
            
    else:
        return {"error":"Tipo no encontrado"}, 404
            
    return {"error":"Personaje no encontrado"}, 404
