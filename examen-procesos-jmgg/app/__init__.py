from flask import Flask
from flask_jwt_extended import JWTManager
from proyectos.routes import proyectosBP
from departamento.routes import departamentoBP
from users.routes import usersBP

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'
jwt = JWTManager(app)

app.register_blueprint (proyectosBP, url_prefix='/proyectos')
app.register_blueprint (departamentoBP, url_prefix='/departamento')
app.register_blueprint(usersBP, url_prefix='/users')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)

