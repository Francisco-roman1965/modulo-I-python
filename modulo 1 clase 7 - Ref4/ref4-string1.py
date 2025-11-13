"""Dada una frase u oración encontrar que palabra es la que tiene más
caracteres y cuántos caracteres tiene
Input: “La programación en Python es poderosa”
Output: “programación” – 12 caracteres"""

print("=== BUSCADOR DE PALABRA MÁS LARGA ===")

# Frase de ejemplo
frase = "La programación en Python es poderosa"
print(f'Input: "{frase}"')

# Dividir la frase en palabras
palabras = frase.split()

# Variables para trackear la palabra más larga
palabra_mas_larga = ""
longitud_maxima = 0

# Buscar la palabra más larga
for palabra in palabras:
    longitud_actual = len(palabra)
    if longitud_actual > longitud_maxima:
        longitud_maxima = longitud_actual
        palabra_mas_larga = palabra

# Mostrar el resultado
print(f'Output: "{palabra_mas_larga}" - {longitud_maxima} caracteres')

# Versión alternativa usando max()
print("\n--- USANDO FUNCIÓN max() ---")
palabra_mas_larga_2 = max(palabras, key=len)
longitud_2 = len(palabra_mas_larga_2)
print(f'Output con max(): "{palabra_mas_larga_2}" - {longitud_2} caracteres')