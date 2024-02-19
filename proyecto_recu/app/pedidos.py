from functions import *
from flask_jwt_extended import jwt_required
from flask import Blueprint, request

rutaPedidos = "ficheros/pedidos.json"
rutaClientes = "ficheros/clientes.json"

pedidosBP = Blueprint("pedidos", __name__)

#Post para añadir un nuevo pedido
@pedidosBP.post("/")
@jwt_required()
def add_pedido():
    pedidos = leeFichero(rutaPedidos)
    clientes = leeFichero(rutaClientes)
    # Se comprueba si está en json
    if request.is_json:
        # Se almacena la peticion en una variable
        pedido = request.get_json()
        #Se comprueba que exista el id de cliente en Clientes
        for cliente in clientes:
            if cliente["id_cliente"] == pedido["id_cliente"]:
                # Se añade el pedido
                pedidos.append(pedido)
                escribeFichero(rutaPedidos, pedidos)
                # Se devuelve el pedido y el codigo de exito
                return pedido, 201
        #Si el id de cliente no existe muestra eror
        return {"error":"Id cliente no encontrado"}, 400
    # Si la petición no es json
    return {"error": "Request must be JSON"}, 415
