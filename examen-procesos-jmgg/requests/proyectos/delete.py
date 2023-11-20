import requests

url="http://localhost:5050/users"

user = {
 "username" : "juanma",
 "password" : "1234"
}

requests.delete(url, json = user)

#Se elimina el proyecto