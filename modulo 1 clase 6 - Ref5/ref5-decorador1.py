"""Crear una función decoradora que dará los buenos días antes de ejecutar una función llamada saludo_inicial(nombre) a ser decorada “Buenos días NOMBRE son las HORA horas con MINUTOS minutos” y luego de ser ejecutada lanzará un mensaje diciendo “Hasta luego NOMBRE que tenga buen día”.
La función a decorar pedirá el nombre de una persona y retornará el mensaje.
Usar la función decorada al menos 3 veces"""

from datetime import datetime

def decorador_saludo(funcion):
    def wrapper():
        nombre = funcion()
        ahora = datetime.now()
        print(f"Buenos días {nombre} son las {ahora.hour} horas con {ahora.minute} minutos")
        print(f"Hasta luego {nombre} que tenga buen día")
        return nombre
    return wrapper

@decorador_saludo
def saludo_inicial():
    nombre = input("Ingrese su nombre: ")
    return nombre

# Usar la función decorada 3 veces
print("=== PRIMER SALUDO ===")
saludo_inicial()

print("\n=== SEGUNDO SALUDO ===")
saludo_inicial()

print("\n=== TERCER SALUDO ===")
saludo_inicial()
