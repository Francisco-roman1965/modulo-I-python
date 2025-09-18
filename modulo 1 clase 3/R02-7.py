"""7. De 3 números asignados mayores a 30 (entre positivos y negativos tú los
propones) a 3 variables, se pide hallar la suma de los valores de los módulos
con 3, 5, y 7 respectivamente, mostrar en pantalla el valor de la suma."""

"Asignación de 3 números mayores a 30 (positivos y negativos)"

numero1 = 35    # Positivo mayor a 30
numero2 = -45   # Negativo mayor a 30 en valor absoluto
numero3 = 32    # Positivo mayor a 30

"Cálculo de los módulos con 3, 5 y 7 respectivamente"
modulo1 = numero1 % 3
modulo2 = numero2 % 5
modulo3 = numero3 % 7

"Suma de los valores de los módulos"
suma_modulos = modulo1 + modulo2 + modulo3

"Mostrar resultados en pantalla"
print("Números asignados:")
print(f"Número 1: {numero1}")
print(f"Número 2: {numero2}")
print(f"Número 3: {numero3}")
print("\nMódulos calculados:")
print(f"{numero1} % 3 = {modulo1}")
print(f"{numero2} % 5 = {modulo2}")
print(f"{numero3} % 7 = {modulo3}")
print(f"\nSuma de los módulos: {suma_modulos}")