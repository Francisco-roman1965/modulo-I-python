"""Ingresar por consola 4 números mediante consola, crear un diccionario
donde los ‘key’ serán los números indicados y los valores serán los cubos de
las estos keys. Mostrar finalmente este diccionario."""

print("Ingrese 4 números:")

# Crear una lista para almacenar los números ingresados
numeros = []

# Ingresar los 4 números
for i in range(4):
    while True:
        try:
            numero = float(input(f"Ingrese el número {i + 1}: "))
            numeros.append(numero)
            break
        except ValueError:
            print("Error: Por favor ingrese un número válido.")

print(f"\nNúmeros ingresados: {numeros}")

# Crear el diccionario donde los keys son los números y los valores son sus cubos
diccionario_cubos = {}

for numero in numeros:
    diccionario_cubos[numero] = numero ** 3

# Mostrar el diccionario resultante
print("\nDiccionario con números y sus cubos:")
print(diccionario_cubos)

# Mostrar de forma más detallada
print("\nDetalle de números y sus cubos:")
for key, value in diccionario_cubos.items():
    print(f"Key: {key} -> Valor (cubo): {value}")