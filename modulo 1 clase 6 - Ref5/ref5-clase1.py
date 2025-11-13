"""Crear una clase Empleado que contenga los siguientes métodos, uno que pida ingresar un nombre, apellido y edad, un método para pedir su sueldo actual y otro método que lo imprima ambos resultados, pero estarán contenidos en un diccionario. Comprobar los métodos instanciando la clase respectivamente al menos para 3 empleados. Considerar en el constructor los valores necesarios."""

class Empleado:
    def __init__(self):
        """Constructor que inicializa los atributos del empleado"""
        self.nombre = ""
        self.apellido = ""
        self.edad = 0
        self.sueldo = 0.0
        self.datos_empleado = {}

    def ingresar_datos_personales(self):
        """Método para ingresar nombre, apellido y edad del empleado"""
        print("\n--- Ingresar Datos Personales ---")
        self.nombre = input("Ingrese el nombre: ")
        self.apellido = input("Ingrese el apellido: ")

        # Validar que la edad sea un número entero positivo
        while True:
            try:
                self.edad = int(input("Ingrese la edad: "))
                if self.edad > 0:
                    break
                else:
                    print("La edad debe ser un número positivo.")
            except ValueError:
                print("Por favor, ingrese un número válido para la edad.")

    def ingresar_sueldo(self):
        """Método para ingresar el sueldo del empleado"""
        print("\n--- Ingresar Sueldo ---")

        # Validar que el sueldo sea un número positivo
        while True:
            try:
                self.sueldo = float(input("Ingrese el sueldo actual: "))
                if self.sueldo >= 0:
                    break
                else:
                    print("El sueldo debe ser un número positivo.")
            except ValueError:
                print("Por favor, ingrese un número válido para el sueldo.")

    def generar_diccionario(self):
        """Método que crea un diccionario con todos los datos del empleado"""
        self.datos_empleado = {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "edad": self.edad,
            "sueldo": self.sueldo
        }
        return self.datos_empleado

    def imprimir_datos(self):
        """Método que imprime los datos del empleado desde el diccionario"""
        datos = self.generar_diccionario()

        print("\n" + "=" * 50)
        print("          DATOS DEL EMPLEADO")
        print("=" * 50)
        print(f"Nombre: {datos['nombre']}")
        print(f"Apellido: {datos['apellido']}")
        print(f"Edad: {datos['edad']} años")
        print(f"Sueldo: ${datos['sueldo']:,.2f}")
        print("=" * 50)
        print(f"Diccionario completo: {datos}")
        print("=" * 50)


# Programa principal para probar la clase
if __name__ == "__main__":
    print("SISTEMA DE GESTIÓN DE EMPLEADOS")
    print("=" * 40)

    # Crear 3 empleados
    empleados = []

    for i in range(3):
        print(f"\n--- Empleado {i + 1} ---")

        # Crear instancia del empleado
        empleado = Empleado()

        # Ingresar datos personales
        empleado.ingresar_datos_personales()

        # Ingresar sueldo
        empleado.ingresar_sueldo()

        # Agregar a la lista de empleados
        empleados.append(empleado)

    # Imprimir datos de todos los empleados
    print("\n" + "=" * 60)
    print("          RESUMEN DE TODOS LOS EMPLEADOS")
    print("=" * 60)

    for i, empleado in enumerate(empleados, 1):
        print(f"\n--- Empleado {i} ---")
        empleado.imprimir_datos()

    # Mostrar todos los diccionarios
    print("\n" + "=" * 60)
    print("          DICCIONARIOS DE TODOS LOS EMPLEADOS")
    print("=" * 60)

    for i, empleado in enumerate(empleados, 1):
        print(f"Empleado {i}: {empleado.generar_diccionario()}")