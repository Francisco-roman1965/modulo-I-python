"""Creando un archivo principal (main.py) donde importará a un módulo (operaciones.py) el cuál contendrá las siguientes funciones:
-Una función que realizará la carga de un valor entero y que verifique que solamente tiene que ser numérico
-Una función que mostrará por pantalla la raíz cuadrada de dicho valor
-Y otra función que calculará el valor elevado al cuadrado y al cubo de dicho número, puedes devolver un diccionario o una lista
-Utilizar el módulo math de python."""

from ref5modulo4 import cargar_numero, calcular_raiz, calcular_potencias

print("=== CALCULADORA MATEMÁTICA ===")
numero = cargar_numero()

print("\n=== RESULTADOS ===")
calcular_raiz(numero)
calcular_potencias(numero)