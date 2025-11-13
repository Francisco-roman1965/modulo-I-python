"""Crea correctamente un diccionario con los campos de: nombre, edad, salario y edad.
Convierte tu diccionario finalmente a una lista y muestra el resultado en la terminal."""

persona = {
    "nombre": "Juan Pérez",
    "edad": 30,
    "salario": 50000.50,
    "edad": 35  # Nota: la clave "edad" se repite, la última asignación prevalece
}

# Mostrar el diccionario original
print("Diccionario original:")
print(persona)
print(f"Tipo de dato: {type(persona)}")
print()

# Convertir el diccionario a una lista
# Opción 1: Convertir a lista de valores
lista_valores = list(persona.values())
print("Lista de valores del diccionario:")
print(lista_valores)
print(f"Tipo de dato: {type(lista_valores)}")
print()

# Opción 2: Convertir a lista de tuplas (clave, valor)
lista_items = list(persona.items())
print("Lista de items (clave, valor):")
print(lista_items)
print(f"Tipo de dato: {type(lista_items)}")
print()

# Opción 3: Convertir a lista de claves
lista_claves = list(persona.keys())
print("Lista de claves del diccionario:")
print(lista_claves)
print(f"Tipo de dato: {type(lista_claves)}")

