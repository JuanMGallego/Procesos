from functions import *
from flask_jwt_extended import jwt_required
from flask import Blueprint, jsonify, request

rutaClientes = "ficheros/clientes.json"
rutaPedidos = "ficheros/pedidos.json"

clientesBP = Blueprint("clientes", __name__)

#Get anidado para pedidr la info del pedido x del cliente y
@clientesBP.get("/<int:id_cliente>/pedidos/<int:id_pedido>")
def get_pedido_cliente(id_cliente, id_pedido):
    clientes = leeFichero(rutaClientes)
    pedidos = leeFichero(rutaPedidos)

    for cliente in clientes:
        if cliente["id_cliente"] == id_cliente:
            for pedido in pedidos:
                if pedido["id_pedido"] == id_pedido:
                    return jsonify(pedido), 200
    return {"error":"Pedido no encontrado"}, 404


#Get para sumar el total de los pedidos por un cliente
@clientesBP.get("/<int:id_cliente>/total")
def get_total_cliente(id_cliente):
    clientes = leeFichero(rutaClientes)
    pedidos = leeFichero(rutaPedidos)

    total = 0.00

    for cliente in clientes:
        if cliente["id_cliente"] == id_cliente:
            for pedido in pedidos:
                if pedido["id_cliente"] == id_cliente:
                    total += pedido["total_pedido"]
            return {"total":str(total)}, 200
    return {"error":"Cliente no encontrado"}, 404

#Put para editar un cliente y añadirlo si no existe
@clientesBP.put("/<int:id_cliente>")
@jwt_required()
def modify_cliente(id):
    clientes = leeFichero(rutaClientes)
    # Se comprueba si la petición es json
    if request.is_json:
        # variable para almacenar el json que llega
        newCliente = request.get_json()
        # Se busca por el id el cliente
        for cliente in clientes:
            if cliente["id_cliente"] == id:
                # Se modifican todos los atributos del cliente por los nuevos
                for element in newCliente:
                    cliente[element] = newCliente[element]
                escribeFichero(rutaClientes, clientes)
                # se devuelve el cliente junto al código de exito
                return cliente, 200
        # Se le asigna un nuevo id    
        cliente["id_cliente"] = find_next_id(rutaClientes)
        # Se añade el cliente
        clientes.append(cliente)
        escribeFichero(rutaClientes, clientes)
        # Se devuelve el cliente en diccionario
        return cliente, 201
    # Si no es json se devuelve un error y el codigo 415
    return {"error": "Request must be JSON"}, 415

#Delete para eliminar un cliente
@clientesBP.delete("/<int:id_cliente>")
@jwt_required()
def delete_cliente(id_cliente):
    clientes = leeFichero(rutaClientes)
    pedidos = leeFichero(rutaPedidos)
    # Se busca el cliente indicado
    for cliente in clientes:
        if cliente["id_cliente"] == id_cliente:
            for pedido in pedidos:
                if pedido["id_cliente"] == id_cliente:
                    pedidos.remove(pedido)
                    escribeFichero(rutaPedidos, pedidos)
            clientes.remove(cliente)
            escribeFichero(rutaClientes, clientes)
            # Si se encuentra el cliente, se devuelve el cliente vacío y el codigo de exito
            return {}, 200
    # Si no se encuentra, se devuelve mensaje de error y codigo 404
    return {"error": "Cliente no encontrado"}, 404
