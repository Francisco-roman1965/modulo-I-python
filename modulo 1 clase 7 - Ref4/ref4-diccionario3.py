"""Crea correctamente un diccionario con los campos de: nombre, edad, salario y edad.
Convierte tu diccionario finalmente a una lista y muestra el resultado en la terminal.
Una vez terminado: Agrega un nuevo key llamado “dni” con su respectivo valor y luego mostrar
el valor del salario y DNI en consola. También elimina el key edad de tu
diccionario, incluyendo su valor. Mostrar finalmente el diccionario actualizado.
Finalmente: Convertir tu diccionario a una lista y mostrar en consola el tipo de datos final que tienes."""

persona = {
    "nombre": "Juan Pérez",
    "edad": 30,
    "salario": 2500.50,
    "edad": 30  # Nota: "edad" aparece dos veces, pero en diccionarios la última clave prevalece
}

print("=== DICCIONARIO ORIGINAL ===")
print(persona)
print(f"Tipo de dato: {type(persona)}")

# Convertir el diccionario a una lista
lista_persona = list(persona.items())
print("\n=== DICCIONARIO CONVERTIDO A LISTA ===")
print(lista_persona)
print(f"Tipo de dato: {type(lista_persona)}")

# Agregar un nuevo key llamado "dni" con su respectivo valor
persona["dni"] = "12345678"
print("\n=== DNI AGREGADO ===")
print(f"DNI agregado: {persona['dni']}")

# Mostrar el valor del salario y DNI en consola
print("\n=== VALORES DE SALARIO Y DNI ===")
print(f"Salario: {persona['salario']}")
print(f"DNI: {persona['dni']}")

# Eliminar el key edad del diccionario, incluyendo su valor
edad_eliminada = persona.pop("edad")
print(f"\n=== EDAD ELIMINADA ===")
print(f"Valor de edad eliminado: {edad_eliminada}")

# Mostrar el diccionario actualizado
print("\n=== DICCIONARIO ACTUALIZADO ===")
print(persona)

# Convertir el diccionario actualizado a una lista
lista_actualizada = list(persona.items())
print("\n=== DICCIONARIO ACTUALIZADO CONVERTIDO A LISTA ===")
print(lista_actualizada)

# Mostrar el tipo de datos final
print("\n=== TIPO DE DATOS FINAL ===")
print(f"Tipo de dato final: {type(lista_actualizada)}")
