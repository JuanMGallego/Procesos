import requests

url="http://localhost:5050/users"

user = {
 "username" : "juanma",
 "password" : "1234"
}

requests.post(url, json = user)

#Se añade el recurso