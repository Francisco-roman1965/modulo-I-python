"""Crear una función que sume los dígitos del número ingresado y muestre
por consola la suma de todos estos dígitos."""

print("=== SUMADOR DE DÍGITOS ===")


def sumar_digitos(numero):
    """
    Función que suma los dígitos del número ingresado
    y muestra por consola la suma
    """
    suma = 0
    # Convertir a string y recorrer cada carácter
    for digito in str(numero):
        # Ignorar el signo negativo si existe
        if digito != '-':
            suma += int(digito)

    # Mostrar el resultado por consola
    print(f"La suma de los dígitos de {numero} es: {suma}")
    return suma


# Solicitar número al usuario
try:
    numero_usuario = int(input("Ingrese un número: "))
    # Usar la función una vez
    sumar_digitos(numero_usuario)
except ValueError:
    print("Por favor, ingrese un número válido.")