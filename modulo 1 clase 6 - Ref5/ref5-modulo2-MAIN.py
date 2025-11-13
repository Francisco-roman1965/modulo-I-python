"""Creando un archivo principal (main.py) donde llamará a un módulo (operaciones.py) el cuál contendrá las siguientes funciones:
-La primera función cargará a 3 números enteros que pedirá al usuario que ingrese por consola un valor.
-La segunda función solamente obtendrá la media de estos valores.
-La última función te indicará cuál es el mayor de los 3 números
-Desde el archivo principal importar al módulo y las funciones correspondiente usando las funciones anteriormente creadas en el módulo.
-Usarlo al menos para 3 casos distintos."""

from ref5modulo2 import cargar_numeros, calcular_media, encontrar_mayor

print("=== CASO 1 ===")
numeros1 = cargar_numeros()
print(f"Números: {numeros1}")
print(f"Media: {calcular_media(numeros1)}")
print(f"Mayor: {encontrar_mayor(numeros1)}")

print("\n=== CASO 2 ===")
numeros2 = cargar_numeros()
print(f"Números: {numeros2}")
print(f"Media: {calcular_media(numeros2)}")
print(f"Mayor: {encontrar_mayor(numeros2)}")

print("\n=== CASO 3 ===")
numeros3 = cargar_numeros()
print(f"Números: {numeros3}")
print(f"Media: {calcular_media(numeros3)}")
print(f"Mayor: {encontrar_mayor(numeros3)}")