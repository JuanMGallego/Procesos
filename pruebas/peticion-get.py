import requests
url = "https://jsonplaceholder.typicode.com/todos/150"

response = requests.get(url)

print("Codigo de estado: ",response.status_code)
print(response.json())


