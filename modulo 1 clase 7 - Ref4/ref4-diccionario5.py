"""Crea correctamente un diccionario con los campos de: nombre, edad, salario y edad.
Convierte tu diccionario finalmente a una lista y muestra el resultado en la terminal.
Una vez terminado: Agrega un nuevo key llamado “dni” con su respectivo valor y luego mostrar
el valor del salario y DNI en consola. También elimina el key edad de tu
diccionario, incluyendo su valor. Mostrar finalmente el diccionario actualizado.
Finalmente: Convertir tu diccionario a una lista y mostrar en consola el tipo de datos final que tienes.
Además: Ingresar el nombre de tu carrera dentro de los valores que tienes en tu diccionario.
- Mostrar en consola los valores de tu carrera y nombre agregándolos a una variable c/u"""

persona = {
    "nombre": "Juan Pérez",
    "edad": 30,
    "salario": 2500.00,
    "edad": 30  # Nota: "edad" está duplicado, se mantendrá el último valor
}

print("Diccionario inicial:")
print(persona)

# Convertir el diccionario a una lista
lista_persona = list(persona.items())
print("\nDiccionario convertido a lista:")
print(lista_persona)

# Agregar un nuevo key llamado "dni" con su respectivo valor
persona["dni"] = "12345678"
print("\nDespués de agregar DNI:")
print(persona)

# Mostrar el valor del salario y DNI en consola
print(f"\nValor del salario: {persona['salario']}")
print(f"Valor del DNI: {persona['dni']}")

# Eliminar el key edad del diccionario, incluyendo su valor
del persona["edad"]
print("\nDespués de eliminar 'edad':")
print(persona)

# Mostrar el diccionario actualizado
print("\nDiccionario actualizado:")
print(persona)

# Convertir el diccionario a una lista
lista_final = list(persona.items())
print("\nDiccionario convertido a lista final:")
print(lista_final)

# Mostrar el tipo de datos final
print(f"\nTipo de datos final: {type(lista_final)}")

# Ingresar el nombre de tu carrera dentro de los valores del diccionario
persona["carrera"] = "Ingeniería de Sistemas"

# Mostrar en consola los valores de carrera y nombre agregándolos a una variable c/u
nombre_variable = persona["nombre"]
carrera_variable = persona["carrera"]

print(f"\nValor de nombre: {nombre_variable}")
print(f"Valor de carrera: {carrera_variable}")

# Mostrar el diccionario final completo
print("\nDiccionario final completo:")
print(persona)

