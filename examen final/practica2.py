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

import random


def crear_lista_aleatoria(cantidad):
    if not isinstance(cantidad, int):
        raise TypeError("La cantidad debe ser entero")

    if cantidad <= 0:
        return []

    numeros = [random.randint(1, 50) for _ in range(cantidad)]
    print(f"Lista con {cantidad} números: {numeros}")
    return numeros


def obtener_no_repetidos(lista_original):
    if not lista_original:
        return []

    unicos = list(set(lista_original))
    print(f"Números no repetidos: {unicos}")
    return unicos


def ordenar_listas(lista):
    if not lista:
        return [], []

    mayor_menor = sorted(lista, reverse=True)
    menor_mayor = sorted(lista)

    print(f"Orden mayor a menor: {mayor_menor}")
    print(f"Orden menor a mayor: {menor_mayor}")

    return mayor_menor, menor_mayor


def mayor_par(lista):
    if not lista:
        return None

    pares = [num for num in lista if num % 2 == 0]

    if not pares:
        print("No hay números pares")
        return None

    mayor = max(pares)
    print(f"Mayor número par: {mayor}")
    return mayor


def acceder_indice(lista, indice):
    try:
        valor = lista[indice]
        print(f"En índice {indice} está el número: {valor}")
        return valor
    except IndexError:
        print(f"Error: Índice {indice} no existe en la lista")
        return None
    except TypeError:
        print("Error: El índice debe ser un número entero")
        return None

