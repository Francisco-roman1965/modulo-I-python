"""Una empresa desea gestionar las facturas pendientes que tiene por pagar,
para esto se creará un diccionario donde tendrá por key el número de factura
“00054” y su value será el coste de la factura. El programa tendrá la opción
de pedir nueva factura (por consola) que se agregará al diccionario. Cada vez
que el área de contabilidad pague una factura se pedirá el número de factura
que fue cancelada, si existe mostrar un mensaje donde indicará “La factura
ya está cancelada” caso contrario “El número de factura no existe”
Considerar que cada vez que se realice algún pago o ingreso de una nueva
factura se mostrará inmediatamente al diccionario actualizado."""

print("=== GESTIÓN DE FACTURAS PENDIENTES ===")

# Diccionario inicial de facturas
facturas = {
    "00054": 1500.00,
    "00055": 2300.50,
    "00056": 800.75
}


def mostrar_facturas():
    """Mostrar facturas actuales"""
    print("\nFacturas pendientes:")
    if facturas:
        for num, costo in facturas.items():
            print(f"  {num}: ${costo:.2f}")
        total = sum(facturas.values())
        print(f"Total pendiente: ${total:.2f}")
    else:
        print("  No hay facturas pendientes")


# Mostrar facturas iniciales
mostrar_facturas()

while True:
    print("\nOpciones:")
    print("1. Agregar factura")
    print("2. Pagar factura")
    print("3. Salir")

    opcion = input("Seleccione (1-3): ")

    if opcion == '1':
        # Agregar nueva factura
        print("\n--- NUEVA FACTURA ---")
        numero = input("Número de factura: ").strip()
        if not numero:
            print(" Número de factura requerido")
            continue

        if numero in facturas:
            print(" Esta factura ya existe")
            continue

        try:
            costo = float(input("Costo: $"))
            if costo <= 0:
                print(" El costo debe ser mayor a 0")
                continue

            facturas[numero] = costo
            print(f" Factura {numero} agregada")
            mostrar_facturas()

        except ValueError:
            print(" Ingrese un costo válido")

    elif opcion == '2':
        # Pagar factura
        print("\n--- PAGAR FACTURA ---")
        if not facturas:
            print("No hay facturas pendientes")
            continue

        numero = input("Número de factura a pagar: ").strip()

        if numero in facturas:
            costo = facturas.pop(numero)  # Elimina y retorna el valor
            print(f" Factura {numero} pagada - ${costo:.2f}")
            mostrar_facturas()
        else:
            print(f" La factura '{numero}' no existe")

    elif opcion == '3':
        # Salir
        print(f"\nResumen final:")
        mostrar_facturas()
        print("¡Hasta pronto!")
        break

    else:
        print(" Opción no válida")