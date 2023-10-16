import requests
url="http://jsonplaceholder.typicode.com/todos/150"
response = requests.get(url)

print("Código de estados: ", response.status_code)
print(response.json())