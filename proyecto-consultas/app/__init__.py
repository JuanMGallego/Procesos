from flask import Flask
from flask_jwt_extended import JWTManager
from .pacientes.routes import pacientesBP
from .medicos.routes import medicosBP
from .usuarios.routes import usuariosBP

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ClAvECoNsUlTaS2004!'
jwt = JWTManager(app)

app.register_blueprint (pacientesBP, url_prefix='/pacientes')
app.register_blueprint (medicosBP, url_prefix='/medicos')
app.register_blueprint(usuariosBP, url_prefix='/usuarios')