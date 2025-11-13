"""Creando un archivo principal (main.py) donde importará a un módulo (operaciones.py) el cuál contendrá las siguientes funciones:
-Una función que realizará la carga de un valor entero y que verifique que solamente tiene que ser numérico
-Una función que mostrará por pantalla la raíz cuadrada de dicho valor
-Y otra función que calculará el valor elevado al cuadrado y al cubo de dicho número, puedes devolver un diccionario o una lista
-Utilizar el módulo math de python."""

import math

def cargar_numero():
    while True:
        try:
            numero = int(input("Ingrese un número entero: "))
            return numero
        except ValueError:
            print("Error: Debe ingresar un número entero válido")

def calcular_raiz(numero):
    if numero >= 0:
        raiz = math.sqrt(numero)
        print(f"Raíz cuadrada de {numero}: {raiz:.2f}")
        return raiz
    else:
        print("No se puede calcular la raíz de un número negativo")
        return None

def calcular_potencias(numero):
    cuadrado = math.pow(numero, 2)
    cubo = math.pow(numero, 3)
    resultados = {
        'cuadrado': cuadrado,
        'cubo': cubo
    }
    print(f"Cuadrado de {numero}: {cuadrado}")
    print(f"Cubo de {numero}: {cubo}")
    return resultados