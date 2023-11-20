import bcrypt
from flask_jwt_extended import create_access_token
from utils.functions import *

from flask import Blueprint, request

ficheroUsers = "ficheros/users.json"

usersBP = Blueprint('users', __name__)

#Post para registrar un usuario
@usersBP.post('/')
def registerUser():
    users = leeFichero(ficheroUsers)
    if request.is_json:
        user = request.get_json()
        password = user['password'].encode('utf-8')
        salt = bcrypt.gensalt()
        hashPassword = bcrypt.hashpw(password, salt).hex()
        user['password'] = hashPassword
        users.append(user)
        escribeFichero(ficheroUsers, users)
        token = create_access_token(identity=user['nombreUser'])
        return {'token': token}, 201
    return {"error": "Request must be JSON"}, 415

#Post para logearte como usuario y recibir el token, además de cifrar la contraseña
@usersBP.get('/')
def loginUser():
    users = leeFichero(ficheroUsers)
    if request.is_json:
        user = request.get_json()
        nombreUser = user['nombreUser']
        password = user["password"].encode('utf-8')
        for userFile in users:
            if userFile['nombreUser'] == nombreUser:
                passwordFile = userFile['password']
                if bcrypt.checkpw(password, bytes.fromhex(passwordFile)):
                    token = create_access_token(identity=nombreUser)
                    return {'token': token}, 200
                else:
                    return {'error': 'No authorized'}, 401
        return {'error': 'User not found'}, 404
    return {"error": "Request must be JSON"}, 415