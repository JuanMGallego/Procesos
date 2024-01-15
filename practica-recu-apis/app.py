from flask import *

app = Flask(__name__)

marcas=[
    {"id":1, "nombre":"Ford", "pais":"EEUU"},
    {"id":2, "nombre":"Renault", "pais":"Alemania"},
    {"id":3, "nombre":"Seat", "pais":"Espana"}
]

@app.get("/marcas")

def get_marcas():
    return jsonify(marcas)


@app.get("/marcas/<int:id>")

def get_marca(id):
    mensaje = {"":""}, 0

    for marca in marcas:
        if marca["id"] == id:
            mensaje = marca, 200
            break

        else:
            mensaje = {"error":"Marca no encontrada"}, 404
        
    return mensaje

@app.post("/marcas")

def buscar_suguiente_id():
    return max(marca["id"] for marca in marcas) + 1

def add_marca():
    mensaje = {"":""}, 0

    if request.is_json:
        marca = request.get_json()
        marca["id"] = buscar_suguiente_id()
        marcas.append(marca)
        mensaje = marca, 201

    else:
        mensaje = {"error":"Marca no encontrada"}, 404

    return mensaje



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)