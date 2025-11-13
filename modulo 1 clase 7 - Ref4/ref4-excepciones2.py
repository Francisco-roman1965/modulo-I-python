"""Crear una función y dentro la respectiva excepción o excepciones para el
siguiente bloque de código para que tu programa no se bloquee, ya que solo
aceptará datos tipos entero y además imprimir un mensaje al usuario la causa
y/o solución. También debe indicar el índice donde ingresarás este nuevo dato,
si el índice está fuera de rango indicárselo al usuario:
lista = [2, 6, 10, 4, 5, 23, 1]
lista[10]: No es posible ingresar el dato, índice fuera de rango
- Usarás dos tipos diferentes de excepciones (IndexError TypeError) y
- Usarás la función al menos 3 veces incluyendo un caso de error"""

print("=== MANEJADOR DE EXCEPCIONES PARA LISTA ===")


def modificar_lista(lista, indice, valor):
    """
    Función que modifica una lista manejando IndexError y TypeError
    """
    try:
        lista[indice] = valor
        print(f"✅ Modificación exitosa: lista[{indice}] = {valor}")
        print(f"   Lista actualizada: {lista}")

    except IndexError:
        print(f"❌ No es posible ingresar el dato, índice {indice} fuera de rango")
        print(f"   La lista tiene {len(lista)} elementos (índices 0-{len(lista) - 1})")

    except TypeError:
        print(f"❌ Error: El índice debe ser un número entero, no {type(indice).__name__}")
        print(f"   Solución: Use un número entero como índice")


# Lista inicial
lista = [2, 6, 10, 4, 5, 23, 1]
print(f"Lista inicial: {lista}")

# Usar la función al menos 3 veces incluyendo un caso de error

# Caso 1: Modificación exitosa
print("\n--- Caso 1: Modificación exitosa ---")
modificar_lista(lista, 2, 100)

# Caso 2: IndexError (índice fuera de rango)
print("\n--- Caso 2: IndexError ---")
modificar_lista(lista, 10, 50)

# Caso 3: TypeError (índice no entero)
print("\n--- Caso 3: TypeError ---")
modificar_lista(lista, "dos", 75)

# Caso adicional: Otro caso exitoso
print("\n--- Caso 4: Otra modificación exitosa ---")
modificar_lista(lista, 0, 999)


