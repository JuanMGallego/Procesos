from flask_jwt_extended import jwt_required
from utils.functions import *
from flask import Blueprint, jsonify, request

rutaFichero = "ficheros/proyectos.json"

proyectosBP = Blueprint('proyectos', __name__)

#Get de todos los proyectos
@proyectosBP.get('/')
def get_proyectos():
    proyectos = leeFichero(rutaFichero)
    return jsonify(proyectos)

#Post para añadir un nuevo proyecto
@proyectosBP.post("/")
def add_proyecto():
    proyectos = leeFichero(rutaFichero)
    if request.is_json:
        proyecto = request.get_json()
        proyecto["id"] = find_next_id(rutaFichero)
        proyectos.append(proyecto)
        escribeFichero(rutaFichero, proyectos)
        return proyecto, 201
    return {"error": "Request must be JSON"}, 415

#Delete para borrar un proyecto
@proyectosBP.delete("/<int:id>")
@jwt_required
def delete_proyecto(id):
    proyectos = leeFichero(rutaFichero)
    for proyecto in proyectos:
        if proyecto['id'] == id:
            proyectos.remove(proyecto)
            return "{}", 200
    return {"error" : "Proyecto no encontrado"}, 404