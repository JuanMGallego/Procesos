import secrets
import string
from flask_jwt_extended import JWTManager
from flask import *
from comics import comicsBP
from personajes import personajesBP
from users import usersBP

alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for i in range(8))

app = Flask(__name__)
app.config['SECRET_KEY'] = password
jwt = JWTManager(app)

app.register_blueprint(comicsBP, url_prefix="/comics")
app.register_blueprint(personajesBP, url_prefix="/personajes")
app.register_blueprint(usersBP, url_prefix="/users")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5050)