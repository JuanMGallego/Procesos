import requests
api_url = "https://localhost:5050/clientes/1"
response = requests.get(api_url)
print(response.json())

cliente = {"id_cliente":1, "nombre_cliente":"Juanma Gallego", "numero_telefono":"423-123-4354"}

response = requests.put(api_url, json=cliente)
print(response.json())
print(response.status_code)