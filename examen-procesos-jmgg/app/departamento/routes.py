from flask_jwt_extended import jwt_required
from utils.functions import *
from flask import Blueprint, jsonify, request

ficheroDepartamento = "app/ficheros/departamento.json"
ficheroProyectos = "app/ficheros/proyectos.json"

departamentoBP = Blueprint('departamento', __name__)

#Get de un departamento
@departamentoBP.get("/<int:id>")
def get_departamento(id):
    departamentos = leeFichero(ficheroDepartamento)
    for departamento in departamentos:
        if departamento['id'] == id:
            return departamento, 200
    return {"error", "Departamento no encontrado"}, 404

#Get anidado
@departamentoBP.get('/<int:id>/proyectos')
def get_proyectos(id):
    list = []
    proyectos = leeFichero(ficheroProyectos)
    for proyecto in proyectos:
        if proyecto['IdDepartamento'] == id:
            list.append(proyecto)
    if len(list) > 0:
        return list, 200
    else:
        return {"error" : "No existen proyectos para este departamento"}, 404
    
#Put del departamento
@departamentoBP.put("/<int:id>")
@jwt_required
def modify_departamento(id):
    departamentos = leeFichero(ficheroDepartamento)
    if request.is_json:
        newDepartamento = request.get_json()
        for departamento in departamentos:
            if departamento["id"] == id:
                for element in newDepartamento:
                    departamento[element] = newDepartamento[element]
                return departamento, 200
    return {"error" : "Request tiene que ser JSON"}, 415