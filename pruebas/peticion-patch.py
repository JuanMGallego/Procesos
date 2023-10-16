import requests
url = "https://jsonplaceholder.typicode.com/todos/6"

dict = {'userId': 5}
response = requests.patch(url, json=dict)

print("Codigo de estado: ",response.status_code)
print(response.json())
