from flask import Blueprint, jsonify, request
from utils.functions import *

ficheroCoches = "app/ficheros/coches"

cochesBP = Blueprint("coches", __name__)
