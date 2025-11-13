"""Escribir un programa donde ingresarás el tamaño de la lista mediante consola, este tamaño servirá para ingresar una cantidad X de nombres de alumnos. Ingresarás los nombres mediante consola también.
Se quiere mostrar finalmente el tamaño de la lista y todos los nombres de la lista que fueron ingresados."""

def main():
    # Solicitar el tamaño de la lista
    while True:
        try:
            tamaño = int(input("Ingrese el tamaño de la lista de alumnos: "))
            if tamaño > 0:
                break
            else:
                print("Por favor, ingrese un número mayor a 0.")
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

    # Crear una lista vacía para almacenar los nombres
    lista_alumnos = []

    # Ingresar los nombres de los alumnos
    print(f"\nIngrese los nombres de los {tamaño} alumnos:")

    for i in range(tamaño):
        while True:
            nombre = input(f"Nombre del alumno {i + 1}: ").strip()
            if nombre:  # Verificar que no esté vacío
                lista_alumnos.append(nombre)
                break
            else:
                print("El nombre no puede estar vacío. Intente nuevamente.")

    # Mostrar los resultados
    print("\n" + "=" * 50)
    print("RESULTADOS:")
    print("=" * 50)
    print(f"Tamaño de la lista: {len(lista_alumnos)} alumnos")
    print("\nNombres de los alumnos ingresados:")

    for i, alumno in enumerate(lista_alumnos, 1):
        print(f"{i}. {alumno}")


if __name__ == "__main__":
    main()