import requests
url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.delete(url)

print("Codigo de estado: ",response.status_code)
print(response.json())