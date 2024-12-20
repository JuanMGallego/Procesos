from flask import Blueprint, jsonify
from utils.functions import *

rutaFichero = "proyecto-paises/ficheros/cities.json"
citiesBP = Blueprint('cities', __name__)

@citiesBP.get('/')
def get_cities():
    cities = leeFichero(rutaFichero)
    return jsonify(cities)

@citiesBP.get("<int:id>")
def get_city(id):
    cities = leeFichero()
    for city in cities:
        if city['id'] == id:
            return city, 200
        return {"error", "City not found"}, 404