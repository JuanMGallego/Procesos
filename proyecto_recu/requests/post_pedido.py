import requests
api_url = "https://localhost:5050/pedido"

pedido = {"id_pedido":1, "fecha_pedido":"2024-01-19", "total_pedido":245.50, "id_cliente":1}
response = requests.post(api_url, json=pedido)

print(response.json())

print("Codigo de estado:", response.status_code)