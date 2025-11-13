"""Entradas y salidas"""
"""Referenciar a dos o más variables con sus respectivos datos"""
"""Asignación múltiple"""

var_1 = input("Ingresa usuario: ")
var_2 = input("Ingresa nombre: ")
var_3 = input("Ingresa edad: ")

#usuario = var_1
#nombre = var_2
#edad = var_3

usuario, nombre, edad = var_1, var_2, var_3

print("Su usuario es: {} y usted tiene {} años".format(usuario, edad))