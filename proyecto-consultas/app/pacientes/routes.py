from flask_jwt_extended import jwt_required
from utils.functions import *
from flask import Blueprint, jsonify, request

rutaFichero = "ficheros/pacientes.json"
pacientesBP = Blueprint('pacientes', __name__)


def find_next_id():
    pacientes = leeFichero(rutaFichero)
    max = pacientes[0]["id"]
    for paciente in pacientes:
        if paciente["id"] > max:
            max = paciente["id"]

    return max+1

@pacientesBP.get('/')
def get_pacientes():
    pacientes = leeFichero (rutaFichero)
    return jsonify(pacientes)

@pacientesBP.get("<int:id>")
def get_paciente(id):
    pacientes = leeFichero (rutaFichero)
    for paciente in pacientes:
        if paciente['id'] == id:
            return paciente, 200
    return {"error", "Paciente not found"}, 404

@pacientesBP.post("/")
@jwt_required()
def add_paciente():
    pacientes = leeFichero(rutaFichero)
    if request.is_json:
        paciente = request.get_json()
        paciente["id"] = find_next_id()
        pacientes.append(paciente)
        escribeFichero(rutaFichero, pacientes)
        return paciente, 201
    return {"error": "Request must be JSON"}, 415

@pacientesBP.put("/<int:id>")
@pacientesBP.patch("/<int:id>")
@jwt_required()
def modify_paciente(id):
    pacientes = leeFichero(rutaFichero)
    if request.is_json:
        newPaciente = request.get_json()
        for paciente in pacientes:
            if paciente["id"] == id:
                for element in newPaciente:
                    paciente[element] = newPaciente[element]
                escribeFichero(rutaFichero, pacientes)
                return paciente, 200
    return {"error": "Request must be JSON"}, 415

@pacientesBP.delete("/<int:id>")
@jwt_required()
def delete_paciente(id):
    pacientes = leeFichero(rutaFichero)
    for paciente in pacientes:
        if paciente['id'] == id:
            pacientes.remove(paciente)
            escribeFichero(rutaFichero, pacientes)
            return {}, 200
    return {"error": "Paciente not found"}, 404