from flask import Flask
from .pacientes.routes import pacientesBP
from .medicos.routes import medicosBP

app = Flask (__name__)

app.register_blueprint (pacientesBP, url_prefix='/pacientes')
app.register_blueprint (medicosBP, url_prefix='/medicos')