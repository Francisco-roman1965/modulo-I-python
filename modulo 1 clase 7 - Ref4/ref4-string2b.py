def cuenta_vocales(texto):
    texto = texto.lower()
    vocales = 'aeiou'
    resultado = {}

    for v in vocales:
        resultado[v] = texto.count(v)

    return resultado


# Probar con un ejemplo
frase = "Programación en Python"
print(f'Frase: "{frase}"')

conteo = cuenta_vocales(frase)
print("Vocales encontradas:")

for vocal, total in conteo.items():
    print(f"{vocal} -> {total}")

# Ahora que el usuario pruebe
print("\n--- Ahora prueba tú ---")
user_frase = input("Escribe una frase: ")

if user_frase:
    user_conteo = cuenta_vocales(user_frase)
    print(f'\nEn "{user_frase}":')

    for v, n in user_conteo.items():
        print(f"{v}: {n}")
else:
    print("No escribiste nada")