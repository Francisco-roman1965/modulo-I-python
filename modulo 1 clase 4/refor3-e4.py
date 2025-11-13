"""Crea un programa que tome un número decimal (con 6 número en la parte decimal) e imprima ese número con:
1 decimal, 2 decimales y 4 decimales"""

def formatear_numero():
    """
    Programa que toma un número decimal y lo imprime con diferentes formatos
    """

    try:
        # Solicitar al usuario un número decimal
        numero_str = input("Ingrese un número decimal (ej: 123.456789): ")

        # Convertir a float y mostrar con diferentes formatos
        numero = float(numero_str)

        print("\nResultados:")
        print(f"Número original: {numero}")
        print(f"1 decimal: {numero:.1f}")
        print(f"2 decimales: {numero:.2f}")
        print(f"4 decimales: {numero:.4f}")

        # Mostrar también el formato original para comparar
        if '.' in numero_str:
            print(f"\nFormato original (como texto): {numero_str}")

    except ValueError:
        print("Error: Por favor ingrese un número válido.")


# Ejecutar el programa
if __name__ == "__main__":
    print("=== FORMATO DE NÚMEROS DECIMALES ===")
    formatear_numero()