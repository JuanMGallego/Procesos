import requests
url = "https://jsonplaceholder.typicode.com/users/1/todos"

dict = {'userId':2, 'title': 'Hacer tareas', 'completed':False}
response = requests.post(url, json=dict)

print("Codigo de estado: ",response.status_code)
print(response.json())