"""3. Tenga las siguientes excepciones:
o Si el texto está vacío, debe lanzar un ValueError("El precio no puede estar vacío").
o Si el texto contiene caracteres inválidos (ejemplo: "abc", "12a3"), debe lanzar un ValueError("Formato de precio inválido").
o Si el número es negativo, debe lanzar un ValueError("El precio no puede ser negativo").
- El programa debe pedir tres precios al usuario, usar la función convertir_precio y almacenarlos en una lista.
- Finalmente, mostrar:
o La lista con los precios convertidos.
o El precio promedio de los tres valores ingresados.
Ejemplo:
Entrada:
Ingrese precio 1: 100.69
Ingrese precio 2: -45
Ingrese precio 3: abc
Salida:
Error: el precio no puede ser negativo
Error: Formato de precio inválido
Precios válidos ingresados: [100.69]
Promedio: 100.5
"""


def convertir_precio(texto: str) -> float:
    """
    Convierte un string a float representando un precio en soles.

    Args:
        texto (str): String que representa un precio

    Returns:
        float: Precio convertido a número decimal

    Raises:
        ValueError: Si el texto está vacío, contiene caracteres inválidos o es negativo
    """
    # Verificar si el texto está vacío
    if not texto.strip():
        raise ValueError("El precio no puede estar vacío")

    # Intentar convertir a float
    try:
        precio = float(texto)
    except ValueError:
        raise ValueError("Formato de precio inválido")

    # Verificar si el precio es negativo
    if precio < 0:
        raise ValueError("El precio no puede ser negativo")

    return precio


def main():
    """
    Función principal que solicita tres precios al usuario y muestra los resultados.
    """
    precios_validos = []

    print("=== CONVERSOR DE PRECIOS ===")

    # Solicitar tres precios al usuario
    for i in range(1, 4):
        try:
            precio_str = input(f"Ingrese precio {i}: ")
            precio_convertido = convertir_precio(precio_str)
            precios_validos.append(precio_convertido)

        except ValueError as e:
            print(f"Error: {e}")

    # Mostrar resultados
    print("\n" + "=" * 40)
    print("RESULTADOS:")
    print(f"Precios válidos ingresados: {precios_validos}")

    if precios_validos:
        promedio = sum(precios_validos) / len(precios_validos)
        print(f"Promedio: {promedio:.2f}")
    else:
        print("No se ingresaron precios válidos")


# Ejecutar el programa
if __name__ == "__main__":
    main()

