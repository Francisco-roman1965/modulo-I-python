"""13. Crea un programa que convierta una temperatura en grados Celsius a
Fahrenheit. La fórmula que tiene que tener en cuenta es la siguiente:
F = (C * 9)/5 + 32
Deberá imprimir algo como lo siguiente:
La temperatura en °C: 30
Temperatura en Fahrenheit: 86.00
Realizarlo con dos distintos datos para la temperatura en Celsius (usar dos
variables iniciales para obtener dos temperaturas finales en Fahrenheit)"""

"Programa para convertir temperaturas con entrada del usuario"

"Primera temperatura"
celsius1 = float(input("Ingrese la primera temperatura en °C: "))
fahrenheit1 = (celsius1 * 9) / 5 + 32

print(f"La temperatura en °C: {celsius1}")
print(f"Temperatura en Fahrenheit: {fahrenheit1:.2f}")
print()

"Segunda temperatura"
celsius2 = float(input("Ingrese la segunda temperatura en °C: "))
fahrenheit2 = (celsius2 * 9) / 5 + 32

print(f"La temperatura en °C: {celsius2}")
print(f"Temperatura en Fahrenheit: {fahrenheit2:.2f}")