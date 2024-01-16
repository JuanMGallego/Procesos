import requests
api_url = "https://localhost:5050/clientes/1"
response = requests.get(api_url)
print(response.status_code)
print(response.json())