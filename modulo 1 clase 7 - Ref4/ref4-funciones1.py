"""Pedir dos números positivos mediante terminal al usuario. Mostrar
como salida el número cuya sumatoria de dígitos es el mayor y los números
cuya sumatoria de dígitos es menor que 10. Utilizar una o más funciones, según
sea conveniente."""

print("=== CALCULADORA DE SUMATORIA DE DÍGITOS ===")


def calcular_sumatoria_digitos(numero):
    """Función para calcular la sumatoria de los dígitos de un número"""
    suma = 0
    numero_str = str(abs(numero))  # Convertir a string y usar valor absoluto

    for digito in numero_str:
        suma += int(digito)

    return suma

def solicitar_numero_positivo(mensaje):
    """Función para solicitar un número positivo al usuario"""
    while True:
        try:
            numero = int(input(mensaje))
            if numero > 0:
                return numero
            else:
                print("Error: El número debe ser positivo. Intente nuevamente.")
        except ValueError:
            print("Error: Ingrese un número entero válido.")

def main():
    """Función principal del programa"""
    # Solicitar dos números positivos
    print("Ingrese dos números positivos:")
    numero1 = solicitar_numero_positivo("Primer número: ")
    numero2 = solicitar_numero_positivo("Segundo número: ")

    # Calcular sumatorias
    sumatoria1 = calcular_sumatoria_digitos(numero1)
    sumatoria2 = calcular_sumatoria_digitos(numero2)

    # Mostrar resultados
    print("\n" + "= " *50)
    print("RESULTADOS")
    print("= " *50)

    print(f"Número 1: {numero1} -> Sumatoria de dígitos: {sumatoria1}")
    print(f"Número 2: {numero2} -> Sumatoria de dígitos: {sumatoria2}")

    # Determinar número con mayor sumatoria
    if sumatoria1 > sumatoria2:
        print(f"\n El número con MAYOR sumatoria de dígitos es: {numero1} (sumatoria = {sumatoria1})")
    elif sumatoria2 > sumatoria1:
        print(f"\n El número con MAYOR sumatoria de dígitos es: {numero2} (sumatoria = {sumatoria2})")
    else:
        print(f"\n Ambos números tienen la MISMA sumatoria de dígitos: {sumatoria1}")

    # Mostrar números con sumatoria menor que 10
    print(f"\n Números con sumatoria de dígitos MENOR que 10:")
    numeros_menor_10 = []

    if sumatoria1 < 10:
        numeros_menor_10.append((numero1, sumatoria1))
        print(f"   • {numero1} (sumatoria = {sumatoria1})")

    if sumatoria2 < 10:
        numeros_menor_10.append((numero2, sumatoria2))
        print(f"   • {numero2} (sumatoria = {sumatoria2})")

    if not numeros_menor_10:
        print("   Ninguno de los números tiene sumatoria menor que 10")

# Ejecutar el programa
if __name__ == "__main__":
    main()