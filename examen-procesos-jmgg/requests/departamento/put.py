import requests

url="http://localhost:5050/users"

user = {
 "username" : "juanma",
 "password" : "1234"
}

requests.get(url, json = user)

header = {'Authorization' : 'Bearer jfbabfasbfasbfyabsfasuf'}

newPaciente = {
 "dni": "123456789A",
 "Nombre": "Francisco",
 "Apellidos": "Somanta Palos",
 "SegSocial": "987654321",
 "FNacimiento": "1990-05-30",
 "idMedico": 1
}
response = requests.post(url, headers = header, json = newPaciente)