from flask import Blueprint, jsonify

rutaFichero = "proyecto\files\medicos.json"
medicosBP = Blueprint('medicos', __name__)

@medicosBP.get('/')
def get_medicos():
    meidcos = leeFichero()
    return jsonify(medicos)

@medicosBP.get("<int:id>")
def get_meidco(id):
    medicos leeFichero()
    for medico in medicos: