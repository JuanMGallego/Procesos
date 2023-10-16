import requests
api_url ="http://locaclhost:5050/countries"

dict = {"name": "Espana", "capital": "Madrid", "area": 51320}
response = requests.post(api_url,json=dict)

print(response.json())
print("Codigo de estado:", response.status_code)