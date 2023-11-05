import bcrypt
from flask_jwt_extended import create_access_token
from utils.functions import *

from flask import Blueprint, request

ficheroUsuarios = "ficheros/usuarios.json"

usuariosBP = Blueprint('usuarios', __name__)


@usuariosBP.post('/')
def registerUsuario():
    usuarios = leeFichero(ficheroUsuarios)
    if request.is_json:
        usuario = request.get_json()
        password = usuario['contrasena'].encode('utf-8')
        salt = bcrypt.gensalt()
        hashPassword = bcrypt.hashpw(password, salt).hex()
        usuario['password'] = hashPassword
        usuarios.append(usuario)
        escribeFichero(ficheroUsuarios, usuarios)
        token = create_access_token(identity=usuario['nombreUsuario'])
        return {'token': token}, 201
    return {"error": "Request must be JSON"}, 415

@usuariosBP.get('/')
def loginUsuario():
    usuarios = leeFichero(ficheroUsuarios)
    if request.is_json:
        usuario = request.get_json()
        nombreUsuario = usuario['nombreUsuario']
        contrasena = usuario["contrasena"].encode('utf-8')
        for usuarioFile in usuarios:
            if usuarioFile['usuarioname'] == nombreUsuario:
                contrasenaFile = usuarioFile['contrasena']
                if bcrypt.checkpw(contrasena, bytes.fromhex(contrasenaFile)):
                    token = create_access_token(identity=nombreUsuario)
                    return {'token': token}, 200
                else:
                    return {'error': 'No authorized'}, 401
        return {'error': 'User not found'}, 404
    return {"error": "Request must be JSON"}, 415