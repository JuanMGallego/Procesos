import requests
api_url = "http://localhost:5050/clientes/1/total"
response = requests.get(api_url)
print(response.json())