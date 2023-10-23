from flask import Blueprint, jsonify

rutaFichero = "proyecto\files\cities.json"
citiesBP = Blueprint('cities', __name__)

@citiesBP.get('/')
def get_cities():
    cities = leeFichero()
    return jsonify(cities)

@citiesBP.get("<int:id>")
def get_city(id):
    cities leeFichero()
    for city in cities: