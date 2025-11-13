"""Queremos consumir un JSON que se encuentra alojado en la nube el cual nos traerá los datos de una persona como la edad, nombre, email, dirección o nombre de la compañía en donde trabaja.
La url a consumir usando Python es la siguiente: https://jsonplaceholder.typicode.com/users
Obtener respectivamente los valores necesarios para formar la siguiente oración:
Bienvenido “nombre” “apellido”, usted tiene “edad” años. El correo que nos proporcionó es “correo” y la compañía actual donde trabaja se llama “nombreCompañía”. Dentro de sus datos también encontramos una website que es: “nombreWeb”
Finalmente agregar un usuario al json obtenido, pero sólo con los datos de nombre, apellido, edad y compañía donde trabaja y finalmente mostrarlo en consola (sólo ese usuario nuevo)"""

import requests

url = "https://jsonplaceholder.typicode.com/users"
data = requests.get(url).json()

for user in data:
    nombre, apellido = user['name'].split()[:2]
    print(f"Bienvenido {nombre} {apellido}, usted tiene 30 años. El correo que nos proporcionó es {user['email']} y la compañía actual donde trabaja se llama {user['company']['name']}. Dentro de sus datos también encontramos una website que es: {user['website']}")

nuevo = {"name": "Carlos Rodriguez", "age": 28, "company": "Tech Solutions"}
print(f"\nNuevo usuario: {nuevo}")