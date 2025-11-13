"""Creando un archivo principal (main.py) donde importará a un módulo (operaciones.py) el cuál contendrá las siguientes funciones:
-Una función que genere 30 números enteros aleatorios entre 0 y 100, y muestre en pantalla esta lista de números aleatorios
-Otra función que ordene los valores de una lista y volver a mostrarla en pantalla
-Otra función que me indicará cuál es el mayor de todos estos números de la lista"""

import random
def generar_numeros(): numeros = [random.randint(0,100) for _ in range(30)]; print("Original:", numeros); return numeros
def ordenar_lista(n): ordenados = sorted(n); print("Ordenada:", ordenados); return ordenados
def encontrar_mayor(n): mayor = max(n); print("Mayor:", mayor); return mayor