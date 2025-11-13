"""Creando un archivo principal (main.py) donde importará a un módulo (operaciones.py) el cuál contendrá las siguientes funciones:
-Una función que genere 30 números enteros aleatorios entre 0 y 100, y muestre en pantalla esta lista de números aleatorios
-Otra función que ordene los valores de una lista y volver a mostrarla en pantalla
-Otra función que me indicará cuál es el mayor de todos estos números de la lista"""

from ref5modulo3 import generar_numeros, ordenar_lista, encontrar_mayor
nums = generar_numeros()
ordenar_lista(nums)
encontrar_mayor(nums)

