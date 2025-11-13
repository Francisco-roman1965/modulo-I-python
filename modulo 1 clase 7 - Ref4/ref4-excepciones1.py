"""Crear una función llamada division_segura(a, b) que recibirá dos
números e intentará devolver la división de a entre b
Si b es cero, debe capturar la excepción y mostrar mensaje “Error: no puedes
dividir entre cero”
Si ambos valores son válidos deben imprimir el resultado Independientemente
del resultado, debe imprimir “Operación finalizada” al final
- Usar try, except, finally
- Valida que los datos ingresados sean numéricos de lo contrario mostrar
“Error: Entrada no numérica”
- Usarás la función al menos 3 veces incluyendo un caso de error"""

print("=== FUNCIÓN DIVISIÓN SEGURA ===")


def division_segura(a, b):
    """
    Función que realiza división segura con manejo de excepciones
    Usa try, except, finally
    """
    try:
        # Convertir a números y realizar división
        num1 = float(a)
        num2 = float(b)
        resultado = num1 / num2
        print(f"Resultado: {resultado}")
        return resultado

    except ZeroDivisionError:
        print("Error: no puedes dividir entre cero")
        return None
    except ValueError:
        print("Error: Entrada no numérica")
        return None
    finally:
        print("Operación finalizada")


# Usar la función al menos 3 veces incluyendo un caso de error

# Caso 1: División normal
print("Caso 1 - División normal:")
division_segura(10, 2)

# Caso 2: División por cero (error)
print("\nCaso 2 - División por cero:")
division_segura(5, 0)

# Caso 3: Entrada no numérica (error)
print("\nCaso 3 - Entrada no numérica:")
division_segura("abc", 2)

# Caso adicional: Otro caso exitoso
print("\nCaso 4 - División con decimales:")
division_segura(7.5, 2.5)
