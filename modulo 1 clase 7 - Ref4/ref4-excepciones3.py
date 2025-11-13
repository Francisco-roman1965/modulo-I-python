"""Crear una función funciona_indice(persona, indice) y dentro la respectiva
excepción para el siguiente bloque de código para que tu programa no se
bloquee y además imprime un mensaje al usuario: “El índice “nombre_indice”
ingresado no existe en el diccionario”, tipo de datos, etc que más pueden
incurrir para este caso (los datos se pedirán por consola):

persona= {'nombre':'Xavier', 'apellido':'Rodriguez', 'dni':'63325345'}
persona['profesion'] #El índice en este caso no existe

Usar la función al menos 2 veces incluyendo un caso de error"""

print("=== MANEJADOR DE EXCEPCIONES PARA DICCIONARIO ===")


def funciona_indice(persona, indice):
    """
    Función que accede a un diccionario manejando KeyError y TypeError
    """
    try:
        valor = persona[indice]
        print(f" Acceso exitoso: persona['{indice}'] = '{valor}'")
        return valor

    except KeyError:
        print(f" El índice '{indice}' ingresado no existe en el diccionario")
        print(f"   Claves disponibles: {list(persona.keys())}")
        return None

    except TypeError as e:
        print(f" Error de tipo: {e}")
        print(f"   El índice debe ser un tipo válido para diccionarios")
        return None


# Diccionario inicial
persona = {'nombre': 'Xavier', 'apellido': 'Rodriguez', 'dni': '63325345'}
print(f"Diccionario persona: {persona}")

# Usar la función al menos 2 veces incluyendo un caso de error

# Caso 1: Acceso exitoso
print("\n--- Caso 1: Acceso exitoso ---")
funciona_indice(persona, 'nombre')

# Caso 2: KeyError (índice no existente)
print("\n--- Caso 2: KeyError ---")
funciona_indice(persona, 'profesion')

# Caso adicional: Otro caso exitoso
print("\n--- Caso 3: Otro acceso exitoso ---")
funciona_indice(persona, 'apellido')