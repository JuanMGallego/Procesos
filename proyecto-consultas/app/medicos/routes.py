from flask_jwt_extended import jwt_required
from utils.functions import *
from flask import Blueprint, jsonify, request

ficheroMedicos = "ficheros/medicos.json"
ficheroPaciente = "ficheros/pacientes.json"

medicosBP = Blueprint('medicos', __name__)

def find_next_id():
    medicos = leeFichero(ficheroMedicos)
    max = medicos[0]["id"]
    for medico in medicos:
        if medico["id"] > max:
            max = medico["id"]

    return max+1

@medicosBP.get('/')
def get_medicos():
    medicos = leeFichero(ficheroMedicos)
    return jsonify(medicos)

@medicosBP.get("<int:id>")
def get_medico(id):
    medicos = leeFichero(ficheroMedicos)
    for medico in medicos:
        if medico['id'] == id:
            return medico, 200
    return {"error": "Medico not found"}, 404

@medicosBP.post("/")
@jwt_required()
# definimos la función correspondiente
def add_medico():
    medicos = leeFichero(ficheroMedicos)
    # Comprobamos si la petición cumple con el formato json
    if request.is_json:
        # Guardamos el formato JSON
        country = request.get_json()
        # Le asignamos un nuevo id
        country["id"] = find_next_id()
        # Añadimos el nuevo país a nuestra lista
        medicos.append(country)
        escribeFichero(ficheroMedicos, medicos)
        # Devolvemos el país en formato diccionario y 201
        return country, 201
    # Si la petición no cumple con el formato JSON
    return {"error": "Request must be JSON"}, 415

@medicosBP.put("/<int:id>")
@medicosBP.patch("/<int:id>")
@jwt_required()
# definimos la función correspondiente
def modify_medico(id):
    medicos = leeFichero(ficheroMedicos)
    # Se comprueba si la petición que nos ha llegado cumple con el formato json
    if request.is_json:
        # Creamos una variable donde guardamos el formato JSON, que coincide con un diccionario
        newMedico = request.get_json()
        # Tenemos que coger de nuestra lista de países, el país concreto a modificar, para lo cual
        # habrá que buscarlo por su id
        for medico in medicos:
            if medico["id"] == id:
                # Modificamos todos los atributos del país con los nuevos valores indicados en el json
                for element in newMedico:
                    medico[element] = newMedico[element]
                escribeFichero(ficheroMedicos, medicos)
                # Devolvemos el país en formato diccionario y el código 200 para indicar que se ha modificado
                return medico, 200
    # Si la petición no cumple con el formato JSON devuelve un mensaje de error y el código 415
    return {"error": "Request must be JSON"}, 415

@medicosBP.delete("/<int:id>")
@jwt_required()
# Se debe añadir como parámetro de entrada el id que se 
# indica en la dirección
def delete_medico(id):
    medicos = leeFichero(ficheroMedicos)
    # Como hay que eliminar un país concreto, tendremos que buscar 
    # en la lista el id del país que se ha indicado en la petición
    for medico in medicos:
        if medico['id'] == id:
            medicos.remove(medico)
            escribeFichero(ficheroMedicos, medicos)
            # Si se encuentra el país, se devuelve el país ya vacío más el código 200
            return {}, 200
    # Si no se encuentra, se devuelve mensaje de error y código 404
    return {"error": "Medico not found"}, 404

@medicosBP.get("/<int:id>/pacientes")
def get_paciente(id):
    list = []
    pacientes = leeFichero(ficheroPaciente)
    for paciente in pacientes:
        if paciente['idMedico'] == id:
            list.append(paciente)
    if len(list) > 0:
        return list, 200
    else:
        return {"error": "No pacientes for this medico"}, 404