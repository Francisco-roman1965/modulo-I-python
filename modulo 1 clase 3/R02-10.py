"""Crear un programa que tome un número flotante en una
variable con 6 decimales y se imprima de diferentes modos:
- 1 decimal
- 2 decimales
- 4 decimales"""

def main():
    "Solicitar al usuario un número flotante con 6 decimales"
    numero = float(input("Ingrese un número flotante con 6 decimales (ej: 123.456789): "))

    "Mostrar el número con diferentes formatos"
    print(f"\nNúmero original: {numero}")
    print(f"1 decimal: {numero:.1f}")
    print(f"2 decimales: {numero:.2f}")
    print(f"4 decimales: {numero:.4f}")

if __name__ == "__main__":
    main()