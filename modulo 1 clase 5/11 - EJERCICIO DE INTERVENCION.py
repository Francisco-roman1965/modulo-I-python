"""dentro de una empresa se va a solicitar pedir el nombre y apellido del empleado (input),
 distrito de residencia ingresado por teclado,
 sueldo y calculo del bono de fin de año, que será el triple del sueldo mensual menos el 10% del sueldo,
  todos estos datos se van a ingresar a un diccionario.
  Asignar a 3 variables los valores del diccionario, mostrar por la terminal (output) el mensaje de:
   "'nombre'`apellido, recibirá 'bono' soles de fin de año"""

def main():
    # Solicitar datos
    nombre = input("Ingrese el nombre del empleado: ")
    apellido = input("Ingrese el apellido del empleado: ")
    distrito = input("Ingrese el distrito de residencia: ")
    sueldo = float(input("Ingrese el sueldo mensual del empleado: "))

    # Calcular bono
    bono = (3 * sueldo) - (0.10 * sueldo)

    # Crear diccionario
    datos_empleado = {
        'nombre': nombre,
        'apellido': apellido,
        'distrito': distrito,
        'sueldo': sueldo,
        'bono': bono
    }

    # Asignar a variables
    nombre_completo = f"{datos_empleado['nombre']} {datos_empleado['apellido']}"
    monto_bono = datos_empleado['bono']

    # Mostrar resultado
    print(f"'{nombre_completo}', recibirá {monto_bono:.2f} soles de fin de año")


# Ejecutar programa
if __name__ == "__main__":
    main()