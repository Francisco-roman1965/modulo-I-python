"""Crear una función saluda_fecha(nombre, dia, mes, anio) que contendrá una
excepción para el siguiente bloque de código y tu programa no se bloquee.
Además, imprime un mensaje al usuario la causa y/o solución (Pedir
nombre, día, mes, año por consola):
Nombre: No debe recibir un dato numérico, sino decírselo al usuario Día, mes
y año: No debe recibir un dato string, sino decírselo al usuario
cadena = "Hello NOMBRE, hoy estamos DÍA de MES del AÑO"
# Hello Leonardo, hoy estamos 04 de agosto del 2025
Independientemente del resultado, debe imprimir “Operación
finalizada” al final
- Usar try, except, finally
Usar la función al menos 3 veces, incluyendo casos de error"""

print("=== FUNCIÓN SALUDA_FECHA ===")


def saluda_fecha(nombre, dia, mes, año):
    """
    Función que crea saludo con fecha manejando excepciones
    """
    try:
        # Validar tipos de datos
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser texto")
        if not isinstance(dia, (int, float)):
            raise ValueError("El día debe ser número")
        if not isinstance(mes, (int, float)):
            raise ValueError("El mes debe ser número")
        if not isinstance(año, (int, float)):
            raise ValueError("El año debe ser número")

        # Crear mensaje
        meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
                 "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

        mensaje = f"Hello {nombre}, hoy estamos {int(dia):02d} de {meses[int(mes) - 1]} del {int(año)}"
        print(f" {mensaje}")
        return mensaje

    except TypeError:
        print(" Error: El nombre no debe recibir un dato numérico")
        return None
    except ValueError:
        print(" Error: Día, mes y año no deben recibir datos string")
        return None
    finally:
        print(" Operación finalizada")


# Usar la función al menos 3 veces incluyendo casos de error

# Caso 1: Correcto
print("--- Caso 1: Datos correctos ---")
saluda_fecha("Leonardo", 4, 8, 2025)

# Caso 2: Error - Nombre numérico
print("\n--- Caso 2: Nombre numérico ---")
saluda_fecha(123, 15, 6, 2024)

# Caso 3: Error - Fecha como texto
print("\n--- Caso 3: Fecha como texto ---")
saluda_fecha("Maria", "quince", 6, 2024)

# Caso adicional: Otro correcto
print("\n--- Caso 4: Otro caso correcto ---")
saluda_fecha("Ana", 25, 12, 2024)