import requests
api_url1 = "http://localhost:5050/personajes/6"
api_url2 = "http://localhost:5050/personajes/28"

response1 = requests.get(api_url1)
response2 = requests.get(api_url2)

print(response1.json())
print(response2.json())

#Personaje posible de editar
personaje1 = {
    "nombre_real": "Pedro Palardo",
    "nombre_superheroe":"Piter Palard",
    "tipo": "Heroe",
    "afiliacion":"No se que poner", 
    "id_comic": 4
    }

#Personaje no existe
personaje2 = {
    "nombre_real": "Pedro Palardo",
    "nombre_superheroe":"Piter Palard",
    "tipo": "Heroe",
    "afiliacion":"No se que poner", 
    "id_comic": 4
    }

response1 = requests.patch(api_url1, json=personaje1)
print(response1.json())
print(response1.status_code)

response2 = requests.patch(api_url2, json=personaje2)
print(response2.json())
print(response2.status_code)