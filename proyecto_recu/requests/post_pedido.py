import requests
api_url = "http://localhost:5050/pedidos"

pedido = {"id_pedido":107, "fecha_pedido":"2024-01-20", "total_pedido":120.54, "estado_pedido": "Entregado", "id_cliente":8}
response = requests.post(api_url, json=pedido)

print(response.json())

print("Codigo de estado:", response.status_code)