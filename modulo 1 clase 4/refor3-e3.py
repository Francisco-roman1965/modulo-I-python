"""Escribe un programa que reciba dos flotantes, luego estos pasarán a ser convertidos en enteros.
 Indique si el primero es múltiplo del segundo. Usar mod para la verificación si el residuo es 0"""

def main():
    # Solicitar dos números flotantes al usuario
    try:
        numero1 = float(input("Ingrese el primer número flotante: "))
        numero2 = float(input("Ingrese el segundo número flotante: "))

        # Convertir a enteros
        entero1 = int(numero1)
        entero2 = int(numero2)

        print(f"\nNúmeros convertidos a enteros:")
        print(f"Primer número: {entero1}")
        print(f"Segundo número: {entero2}")

        # Verificar si el segundo número es cero para evitar división por cero
        if entero2 == 0:
            print("Error: No se puede dividir por cero.")
            return

        # Verificar si el primero es múltiplo del segundo usando mod
        if entero1 % entero2 == 0:
            print(f"\n{entero1} es múltiplo de {entero2}")
        else:
            print(f"\n{entero1} NO es múltiplo de {entero2}")

    except ValueError:
        print("Error: Por favor ingrese números válidos.")
    except Exception as e:
        print(f"Error inesperado: {e}")


if __name__ == "__main__":
    main()