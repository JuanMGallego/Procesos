import requests

url="http://localhost:5050/departamento/1/proyectos"

user = {
 "username" : "juanma",
 "password" : "1234"
}

r = requests.get(url, json = user)

if (r.status_code == 200):
    print(r.json())
else:
    print("Error el codigo de error es", r.status_code)