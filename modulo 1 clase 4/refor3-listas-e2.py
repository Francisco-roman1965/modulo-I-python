"""Crear un programa en Python donde tendrás una lista con 6 departamentos,
el programa te pedirá ingresar 2 departamentos el cual el segundo departamento que ingreses sustituirá al primero de la lista."""

def main():
    # Lista inicial con 6 departamentos
    departamentos = ["Lima", "Arequipa", "Cusco", "Piura", "La Libertad", "Lambayeque"]

    print("=== PROGRAMA DE MODIFICACIÓN DE DEPARTAMENTOS ===")
    print(f"Lista actual de departamentos: {departamentos}")
    print()

    try:
        # Solicitar el primer departamento a reemplazar
        print("Ingrese el departamento que desea reemplazar:")
        depto_viejo = input("Departamento a sustituir: ").strip().title()

        # Verificar si el departamento existe en la lista
        if depto_viejo not in departamentos:
            print(f"Error: El departamento '{depto_viejo}' no se encuentra en la lista.")
            return

        # Solicitar el nuevo departamento
        print("Ingrese el nuevo departamento:")
        depto_nuevo = input("Nuevo departamento: ").strip().title()

        # Encontrar el índice del departamento a reemplazar
        indice = departamentos.index(depto_viejo)

        # Realizar el reemplazo
        departamentos[indice] = depto_nuevo

        # Mostrar resultados
        print()
        print("=== RESULTADO ===")
        print(f"Se reemplazó '{depto_viejo}' por '{depto_nuevo}'")
        print(f"Lista actualizada: {departamentos}")

    except ValueError:
        print("Error: Ha ocurrido un problema con los datos ingresados.")
    except Exception as e:
        print(f"Error inesperado: {e}")


if __name__ == "__main__":
    main()