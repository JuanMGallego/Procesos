from functions import *
from flask_jwt_extended import jwt_required
from flask import Blueprint, request

rutaPedidos = "ficheros/pedidos.json"

pedidosBP = Blueprint("pedidos", rutaPedidos)

#Post para añadir un nuevo pedido
@pedidosBP.post("/")
@jwt_required
def add_pedido():
    pedidos = leeFichero(rutaPedidos)
    # Se comprueba si está en json
    if request.is_json:
        # Se almacena la peticion en una variable
        pedido = request.get_json()
        # se le asigna un nuevo id
        pedido["id"] = find_next_id()
        # Se añade el pedido
        pedidos.append(pedido)
        escribeFichero(rutaPedidos, pedidos)
        # Se devuelve el pedido y el codigo de exito
        return pedido, 201
    # Si la petición no es json
    return {"error": "Request must be JSON"}, 415