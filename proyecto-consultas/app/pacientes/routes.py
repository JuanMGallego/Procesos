from flask import Blueprint, jsonify

pacientesBP = Blueprint('pacientes', __name__)

@pacientesBP.get('/')
def get_pacientes():
    pacientes = leeFichero (rutaFichero)
    return jsonify(pacientes)

@pacientesBP.get("/<int:id>")
def get_paciente(id):
    pacientes = leeFichero (rutaFichero)
    for paciente in pacientes:
        if paciente['id'] == id: