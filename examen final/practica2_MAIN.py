"""Utilizar el concepto de módulo necesariamente. Y escribir un programa para el
manejo de listas el cuál cumplirá los siguientes requerimientos (2 ptos):
Reglas:
- Crear una función que le permitirá almacenar X números aleatorios en
una lista y finalmente los imprimirá por consola al llamar la función. X
solo puede ser entero. No otro tipo de dato. Y también un índice
existente en la lista (usar para esto excepciones)
- Crear una función que le permita almacenar los números no repetidos de
la lista anterior, la función retornará este valor para que pueda ser
impreso por consola.
- Crear una función donde se creará una lista para ordenar de mayor a
menor la lista que se creó en el ítem anterior (número no repetidos) y
otra lista para ordenarlas de menor a mayor, retornar este valor e
imprimirlos por consola.
- Crear una función para indicar cuál es el mayor número par de la lista
(lista de la regla 2), retornar este valor e imprimirlo por consola.
- Crear el archivo main.py, donde solo llamarás las anteriores funciones que
se encontrarán alojadas en un módulo (probarlo para dos casos mínimo)"""

from practica2 import *

print("=== PRUEBA 1 ===")
lista1 = crear_lista_aleatoria(8)
if lista1:
    acceder_indice(lista1, 2)
    acceder_indice(lista1, 15)

    unicos1 = obtener_no_repetidos(lista1)
    ordenar_listas(unicos1)
    mayor_par(unicos1)

print("\n" + "=" * 50)
print("=== PRUEBA 2 ===")
lista2 = crear_lista_aleatoria(5)
if lista2:
    acceder_indice(lista2, 0)
    acceder_indice(lista2, "hola")

    unicos2 = obtener_no_repetidos(lista2)
    ordenar_listas(unicos2)
    mayor_par(unicos2)

print("\n" + "=" * 50)
print("=== PRUEBA EXTRA ===")
lista3 = crear_lista_aleatoria(3)
if lista3:
    unicos3 = obtener_no_repetidos(lista3)
    ordenar_listas(unicos3)
    mayor_par(unicos3)