from flask import Blueprint, jsonify

countriesBP = Blueprint('countries', __name__)

@countriesBP.get('/')
def get_countries():
    countries = leeFichero (rutaFichero)
    return jsonify(countries)

@countriesBP.get("/<int:id>")
def get_country(id):
    countries = leeFichero (rutaFichero)
    for country in countries:
        if country['id'] == id: