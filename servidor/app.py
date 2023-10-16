from flask import *

app = Flask(__name__)

countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 51320},
    {"id": 2, "name": "Australia", "capital": "Cabberra", "area": 7617930},
    {"id": 3, "name": "Egipto", "capital": "Cairo", "area": 1010408}
]

@app.get("/countries")
def getCountry():
    return jsonify(countries)

@app.get("/countries/<int:id>")
def getCountry(id):

    for country in countries:

        if country['id'] == id:

            return country, 200
            
    return {"error": "Country not found"}, 404

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)

@app.post("/countries")
def addCountry():
    if request.is_json:
        country = request.get_json()