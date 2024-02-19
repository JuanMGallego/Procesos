import requests
api_url = "http://localhost:5050/clientes/1/pedidos/101"
response = requests.get(api_url)
print(response.json())