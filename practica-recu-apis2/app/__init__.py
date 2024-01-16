
from flask import *
from marcas.routes import marcasBP
from coches.routes import cochesBP


app = Flask(__name__)

app.register_blueprint(marcasBP, url_prefix="/marcas")
app.register_blueprint(cochesBP, url_prefix="/coches")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5050)