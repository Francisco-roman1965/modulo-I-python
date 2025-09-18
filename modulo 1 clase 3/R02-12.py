"""12. Escribe un programa que almacene información de un producto: Tu nombre, nombre del producto, precio unitario (float), cantidad (int) e
imprimirá finalmente algo como lo siguiente: Buen día Nombre, el detalle de su compra es el siguiente:
- Producto: Pollo a la brasa
- Precio unitario: 50.50
- Cantidad: 2
- Total a pagar: 101"""

"Programa para almacenar información de un producto y mostrar el detalle de compra"

def main():
    "Solicitar información al usuario"
    nombre_cliente = input("Ingrese su nombre: ")
    nombre_producto = input("Ingrese el nombre del producto: ")

    "Solicitar precio unitario con validación"
    while True:
        try:
            precio_unitario = float(input("Ingrese el precio unitario: "))
            if precio_unitario <= 0:
                print("El precio debe ser mayor a 0. Intente nuevamente.")
                continue
            break
        except ValueError:
            print("Por favor, ingrese un valor numérico válido.")

    "Solicitar cantidad con validación"
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad: "))
            if cantidad <= 0:
                print("La cantidad debe ser mayor a 0. Intente nuevamente.")
                continue
            break
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

    "Calcular total a pagar"
    total_pagar = precio_unitario * cantidad

    "Mostrar el detalle de la compra"
    print("\n" + "=" * 50)
    print(f"Buen día {nombre_cliente}, el detalle de su compra es el siguiente:")
    print("-" * 50)
    print(f"- Producto: {nombre_producto}")
    print(f"- Precio unitario: {precio_unitario:.2f}")
    print(f"- Cantidad: {cantidad}")
    print(f"- Total a pagar: {total_pagar:.2f}")
    print("=" * 50)

"Ejecutar el programa"
if __name__ == "__main__":
    main()