import requests
api_url = "http://localhost:5050/users"

pedido = {"username":"juanma", "password":"ClAvEsEcReTa2004!"}
response = requests.post(api_url, json=pedido)

print(response.json())

print("Codigo de estado:", response.status_code)