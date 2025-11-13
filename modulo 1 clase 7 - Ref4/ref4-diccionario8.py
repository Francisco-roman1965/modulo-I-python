"""Crear una agenda basada en un diccionario donde los key serán los nombres
de las personas y sus “values” serán los números de teléfono de c/u.
Ingresarás por consola el nombre y el número de cada persona que serán
registrados en la agenda.
El programa también te permitirá buscar por nombre en el diccionario en caso
no exista mostrar un mensaje de “No se encuentra registrado en la agenda”"""

print("=== AGENDA TELEFÓNICA BÁSICA ===")

# Crear diccionario para la agenda
agenda = {}

while True:
    print("\nOpciones:")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Salir")

    opcion = input("Seleccione opción (1-3): ")

    if opcion == '1':
        # Agregar contacto
        print("\n--- AGREGAR CONTACTO ---")
        nombre = input("Nombre: ").strip().title()
        telefono = input("Teléfono: ").strip()

        if nombre and telefono:
            agenda[nombre] = telefono
            print(f"Contacto '{nombre}' agregado.")
        else:
            print("Nombre y teléfono son obligatorios.")

    elif opcion == '2':
        # Buscar contacto
        print("\n--- BUSCAR CONTACTO ---")

        if not agenda:
            print("La agenda está vacía.")
            continue

        nombre_buscar = input("Nombre a buscar: ").strip().title()

        if nombre_buscar in agenda:
            print(f"Encontrado: {nombre_buscar} - Teléfono: {agenda[nombre_buscar]}")
        else:
            print(f" '{nombre_buscar}' no se encuentra registrado en la agenda.")

    elif opcion == '3':
        # Salir
        print(f"\n¡Hasta pronto! Contactos en agenda: {len(agenda)}")
        break

    else:
        print(" Opción no válida. Intente nuevamente.")