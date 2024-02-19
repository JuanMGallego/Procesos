import requests
api_url = "http://localhost:5050/comic/1/heroes/1"
response = requests.get(api_url)
print(response.json())

api_url = "http://localhost:5050/comic/1/villanos/2"
response = requests.get(api_url)
print(response.json())

api_url = "http://localhost:5050/comic/1/heroes/2"
response = requests.get(api_url)
print(response.json())

api_url = "http://localhost:5050/comic/1/villanos/23"
response = requests.get(api_url)
print(response.json())

api_url = "http://localhost:5050/comic/1/prueba/1"
response = requests.get(api_url)
print(response.json())