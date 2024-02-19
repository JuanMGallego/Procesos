import requests
api_url = "http://localhost:5050/users"

response = requests.get(api_url)

print(response.json())

usuario = {
    "username":"juanma",
    "pasword":"contra1234"
    }

response = requests.post(api_url, json=usuario)
print(response.json())
print(response.status_code)