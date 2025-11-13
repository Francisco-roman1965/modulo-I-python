"""Crea una función que al ingresar dos números por parámetro mostrará
todos los cuadrados de los números que hay entre ellos (Usar la función una
vez y mostrar el resultado por consola). Los números serán ingresados y
solicitados al usuario."""

print("=== GENERADOR DE CUADRADOS ENTRE NÚMEROS ===")


def mostrar_cuadrados_entre_numeros(inicio, fin):
    """
    Función que muestra todos los cuadrados de los números que hay entre dos números
    """
    print(f"\n Cuadrados de los números entre {inicio} y {fin}:")
    print("-" * 40)

    # Asegurarse de que inicio sea menor que fin
    if inicio > fin:
        inicio, fin = fin, inicio
        print(f"  Nota: Se intercambiaron los números para orden ascendente")

    # Mostrar los cuadrados
    for numero in range(inicio, fin + 1):
        cuadrado = numero ** 2
        print(f"   {numero}² = {cuadrado}")


def solicitar_numero(mensaje):
    """Función para solicitar un número al usuario"""
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print(" Error: Ingrese un número entero válido.")


# Programa principal
def main():
    """Función principal que utiliza la función de cuadrados"""
    print("Ingrese dos números para generar los cuadrados entre ellos:")

    # Solicitar los números al usuario
    numero1 = solicitar_numero("Primer número: ")
    numero2 = solicitar_numero("Segundo número: ")

    print(f"\n Números ingresados: {numero1} y {numero2}")

    # Usar la función una vez como solicita el instructivo
    mostrar_cuadrados_entre_numeros(numero1, numero2)


# Ejecutar el programa
if __name__ == "__main__":
    main()