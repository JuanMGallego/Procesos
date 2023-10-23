from flask import Flask
from .countries.routes import countriesBP
from .cities.routes import citiesBP

app = Flask (__name__)

app.register_blueprint (countries BP, url_prefix='/countries')
app.register_blueprint (citiesBP, url_prefix='/cities')