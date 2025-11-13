"""Crear un programa que cuente cuántas veces aparece cada vocal en la
oración. Ignorar mayúsculas/minúsculas
Input: “Programación en Python”
Output:
a: 2
e: 1
i: 1
o: 2
u: 0
Métodos útiles: lower() y count()"""

print("=== CONTADOR DE VOCALES ===")


def contar_vocales(frase):
    """Función para contar cuántas veces aparece cada vocal en una frase"""

    # Convertir la frase a minúsculas para ignorar mayúsculas/minúsculas
    frase_minusculas = frase.lower()

    # Definir las vocales que vamos a contar
    vocales = 'aeiou'

    # Contar cada vocal usando count()
    conteo = {}
    for vocal in vocales:
        conteo[vocal] = frase_minusculas.count(vocal)

    return conteo


def mostrar_resultado(conteo, frase_original):
    """Función para mostrar el resultado formateado"""
    print(f'\nInput: "{frase_original}"')
    print("Output:")
    for vocal, cantidad in conteo.items():
        print(f"{vocal}: {cantidad}")


# Versión 1: Frase predefinida
print("\n--- VERSIÓN 1: Frase predefinida ---")
frase_ejemplo = "Programación en Python"
conteo_vocales = contar_vocales(frase_ejemplo)
mostrar_resultado(conteo_vocales, frase_ejemplo)

# Versión 2: Ingresar frase por consola
print("\n--- VERSIÓN 2: Ingresar frase por consola ---")
frase_usuario = input("Ingrese una frase: ").strip()

if frase_usuario:
    conteo_usuario = contar_vocales(frase_usuario)
    mostrar_resultado(conteo_usuario, frase_usuario)
else:
    print("No ingresó ninguna frase.")