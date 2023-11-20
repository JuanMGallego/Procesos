import requests

url="http://localhost:5050/departamento/1"

user = {
 "username" : "juanma",
 "password" : "1234"
}

r = requests.get(url, json = user)

if (r.status_code == 200):
    #Imprime las lineas de cada dato del departamento
    print()
else:
    print("Error el codigo de error es", r.status_code)