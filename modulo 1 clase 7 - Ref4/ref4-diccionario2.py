"""Crea correctamente un diccionario con los campos de: nombre, edad, salario y edad.
Convierte tu diccionario finalmente a una lista y muestra el resultado en la terminal.
2. Agrega un nuevo key llamado “dni” con su respectivo valor y luego mostrar
el valor del salario y DNI en consola. También elimina el key edad de tu
diccionario, incluyendo su valor. Mostrar finalmente el diccionario
actualizado."""

persona = {
    "nombre": "Juan Pérez",
    "edad": 30,
    "salario": 2500.00,
    "edad": 30  # Nota: "edad" está duplicado, Python usará el último valor
}

# Mostrar el diccionario original
print("Diccionario original:")
print(persona)
print()

# Convertir el diccionario a una lista
# Nota: Al convertir un diccionario a lista, obtenemos una lista de las claves
lista_persona = list(persona)
print("Diccionario convertido a lista (solo las claves):")
print(lista_persona)
print()

# Si quieres una lista de valores o items completos:
lista_valores = list(persona.values())
lista_items = list(persona.items())

print("Lista de valores:")
print(lista_valores)
print()

print("Lista de items (tuplas clave-valor):")
print(lista_items)
print()

# Agregar un nuevo key llamado "dni" con su respectivo valor
persona["dni"] = "12345678A"

# Mostrar el valor del salario y DNI en consola
print("Valor del salario:", persona["salario"])
print("Valor del DNI:", persona["dni"])
print()

# Eliminar el key edad del diccionario, incluyendo su valor
del persona["edad"]

# Mostrar finalmente el diccionario actualizado
print("Diccionario actualizado:")
print(persona)
print()

# Versión alternativa para mostrar más organizado
print("Diccionario actualizado (formateado):")
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

