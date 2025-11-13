"""Crear un programa usando decoradores para mostrar solo la hora
y el minuto del momento que se usa el decorador
Reglas:
- Al ejecutar el decorador mostrará un mensaje: “El decorador está siendo
ejecutado a las H con m minutos y S segundos”
- Crear la función decorador adecuadamente que sumará los elementos de la
función que pasará como parámetro de la función decoradora
- Crear una función, por ejemplo: usando 6 números e indicar el mayor de
todos ellos (o x números) para decorarla con la función anterior.
- Usar la propiedad de N parámetros para la función a decorar usando sus key
y values (**kwards) para usar más de 6 valores en la función (value_7 = 10,
value_8 = 22, value_9=45) y visualizar los resultados usando el decorador
implementado con un mínimo tres ejemplos."""

import datetime


def decorador_tiempo(func):
    def wrapper(*args, **kwargs):
        ahora = datetime.datetime.now()
        print(
            f"El decorador está siendo ejecutado a las {ahora.hour} con {ahora.minute} minutos y {ahora.second} segundos")

        resultado = func(*args, **kwargs)
        return resultado

    return wrapper


def decorador_suma(func):
    def wrapper(*args, **kwargs):
        todos_numeros = list(args) + list(kwargs.values())

        if not todos_numeros:
            print("No hay números para sumar")
            return 0

        suma_total = sum(todos_numeros)
        print(f"Suma de todos los elementos: {suma_total}")

        resultado = func(*args, **kwargs)
        return resultado

    return wrapper


@decorador_tiempo
@decorador_suma
def encontrar_mayor(*args, **kwargs):
    todos_numeros = list(args) + list(kwargs.values())

    if not todos_numeros:
        print("No hay números")
        return None

    mayor = max(todos_numeros)
    print(f"El mayor número es: {mayor}")
    return mayor


# Probando con diferentes casos
print("=== PRUEBA 1 - 6 números ===")
result1 = encontrar_mayor(15, 8, 23, 45, 12, 9)

print("\n=== PRUEBA 2 - Con kwargs ===")
result2 = encontrar_mayor(5, 18, 3, value_7=10, value_8=22, value_9=45)

print("\n=== PRUEBA 3 - Más números ===")
result3 = encontrar_mayor(1, 2, 3, num4=50, num5=25, num6=30, extra=100)

print("\n=== PRUEBA 4 - Pocos números ===")
result4 = encontrar_mayor(7, 3, num_x=15)

print("\n=== RESULTADOS ===")
print(f"Prueba 1: {result1}")
print(f"Prueba 2: {result2}")
print(f"Prueba 3: {result3}")
print(f"Prueba 4: {result4}")