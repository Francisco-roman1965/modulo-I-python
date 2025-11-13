"""Pedir al usuario que ingrese un nombre y apellidos el cual será usada
por un parámetro para una función que se creará e indicará cuantas letras
tiene el nombre solamente. Usar la función un mínimo de dos veces para dos
personas e indicar quien tiene el nombre con mayor número de caracteres
(condicional)"""

print("=== COMPARADOR DE NOMBRES ===")


def contar_letras_nombre(nombre_completo):
    """
    Función que indica cuántas letras tiene el nombre solamente
    """
    # Obtener el primer nombre
    primer_nombre = nombre_completo.split()[0]
    cantidad_letras = len(primer_nombre)

    print(f"El nombre '{primer_nombre}' tiene {cantidad_letras} letras")
    return cantidad_letras


# Solicitar dos nombres al usuario
print("Ingrese los nombres completos de 2 personas:")

nombre1 = input("Primera persona: ")
nombre2 = input("Segunda persona: ")

print("\n" + "=" * 40)

# Usar la función por primera vez
longitud1 = contar_letras_nombre(nombre1)

# Usar la función por segunda vez
longitud2 = contar_letras_nombre(nombre2)

print("\n" + "=" * 40)

# Determinar quién tiene el nombre más largo
if longitud1 > longitud2:
    print(f"La primera persona tiene el nombre más largo ({longitud1} vs {longitud2} letras)")
elif longitud2 > longitud1:
    print(f"La segunda persona tiene el nombre más largo ({longitud2} vs {longitud1} letras)")
else:
    print(f"Ambos nombres tienen la misma longitud ({longitud1} letras)")