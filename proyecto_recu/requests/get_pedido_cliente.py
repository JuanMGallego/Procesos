import requests
api_url = "https://localhost:5050/clientes/1/pedidos/101"
response = requests.get(api_url)
print(response.json())