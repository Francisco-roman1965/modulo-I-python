"""Crea una lista vacía, luego ingresa sus valores (10 valores numéricos)
 y finalmente muestra la suma y la media de los números ingresado insertados en la terminal"""

def main():
    # Crear una lista vacía
    numeros = []

    print("=== PROGRAMA DE SUMA Y MEDIA ===")
    print("Ingrese 10 valores numéricos:")

    # Ingresar 10 valores numéricos
    for i in range(10):
        while True:
            try:
                # Solicitar cada número
                valor = float(input(f"Ingrese el valor {i + 1}: "))
                numeros.append(valor)
                break
            except ValueError:
                print("Error: Por favor ingrese un valor numérico válido.")

    # Calcular la suma
    suma = sum(numeros)

    # Calcular la media
    media = suma / len(numeros)

    # Mostrar resultados
    print("\n" + "=" * 40)
    print("RESULTADOS:")
    print(f"Lista de números ingresados: {numeros}")
    print(f"Suma de los números: {suma}")
    print(f"Media de los números: {media:.2f}")
    print("=" * 40)


if __name__ == "__main__":
    main()