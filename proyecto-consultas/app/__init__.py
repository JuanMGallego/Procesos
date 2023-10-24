from flask import Flask
from .pacientes.routes import pacientesBP
from .medicos.routes import meicosBP

app = Flask (__name__)

app.register_blueprint (pacientes BP, url_prefix='/pacientes')
app.register_blueprint (medicosBP, url_prefix='/medicos')