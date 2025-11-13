"""Pide al usuario que ingrese una frase y una palabra, obtén si la palabra está
dentro de la oración sin importar si está en mayúsculas o minúsculas.
En caso que aparezca, indica la posición del primer carácter en donde
empieza
Input: frase = “Python y sus enormes ventajas”, palabra = “Python”
Output: “Python aparece en la posición 0”
Métodos útiles: lower() y find()"""

print("=== BUSCADOR SIMPLE DE PALABRAS ===")

# Pedir datos al usuario
frase = input("Ingrese una frase: ").strip()
palabra = input("Ingrese la palabra a buscar: ").strip()

if frase and palabra:
    # Usar lower() para ignorar mayúsculas/minúsculas
    frase_min = frase.lower()
    palabra_min = palabra.lower()

    # Usar find() para encontrar la posición
    posicion = frase_min.find(palabra_min)

    # Mostrar resultado
    print(f'\nInput: frase = "{frase}", palabra = "{palabra}"')

    if posicion != -1:
        print(f'Output: "{palabra}" aparece en la posición {posicion}')
    else:
        print(f'Output: "{palabra}" no aparece en la frase')
else:
    print("Error: Debe ingresar tanto la frase como la palabra.")

