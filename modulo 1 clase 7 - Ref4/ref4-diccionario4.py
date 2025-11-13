"""Crear un diccionario con 6 departamentos del Perú.
- Borrar cualquier departamento, usando la palabra reservada del.
- Actualizar el penúltimo departamento por otro.
- Comprobar que no existe este departamento borrado dentro del diccionario."""

departamentos = {
    1: "Lima",
    2: "Arequipa",
    3: "Cusco",
    4: "Piura",
    5: "La Libertad",
    6: "Junín"
}

print("Departamentos originales:", departamentos)

# 1. Borrar un departamento con del
del departamentos[2]  # Elimina Arequipa
print("Después de eliminar:", departamentos)

# 2. Actualizar el penúltimo departamento
claves = list(departamentos.keys())
penultimo = claves[-2]
departamentos[penultimo] = "Lambayeque"
print("Después de actualizar penúltimo:", departamentos)

# 3. Comprobar que no existe el departamento borrado
if "Arequipa" not in departamentos.values():
    print("Arequipa fue eliminado correctamente")
else:
    print("Arequipa todavía existe")