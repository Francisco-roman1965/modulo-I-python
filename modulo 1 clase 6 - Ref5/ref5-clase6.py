"""Crear una clase PersonaPrestamo que hereda de la clase anterior (problema 5) donde tendrá los métodos: Uno, que indicará si la persona está apta para un préstamo solo si ha estado más de 12 meses trabajando en la empresa en caso contrario se le informa que no es posible darle el préstamo y la otra condición adicional es si su edad es mayor de 25 años.
Agregar un segundo método a esta nueva clase que te indicará si estás aprobado recibirás 10 veces tu sueldo de préstamo, el total de préstamo otorgado es {cantidad_prestamo}.
Instanciar 3 veces la clase para mostrar diferentes resultados."""

from datetime import datetime, date
class Persona:
    def __init__(self, nombre="", edad=0, fecha_ingreso="", sueldo=0):
        self.nombre = nombre
        self.edad = edad
        self.fecha_ingreso = fecha_ingreso
        self.sueldo = sueldo

    def inicializar_datos(self):
        # Validar nombre (no vacío)
        while True:
            self.nombre = input("Nombre: ").strip()
            if self.nombre:  # Verificar que no esté vacío
                break
            else:
                print("Error: El nombre no puede estar vacío")

        # Validar edad (número entero positivo)
        while True:
            try:
                edad_input = input("Edad: ").strip()
                if edad_input:  # Verificar que no esté vacío
                    self.edad = int(edad_input)
                    if self.edad > 0:
                        break
                    else:
                        print("Error: La edad debe ser mayor a 0")
                else:
                    print("Error: La edad no puede estar vacía")
            except ValueError:
                print("Error: Ingrese un número válido para la edad")

        # Validar fecha (formato correcto)
        while True:
            self.fecha_ingreso = input("Fecha ingreso (dd/mm/aaaa): ").strip()
            if self.fecha_ingreso:  # Verificar que no esté vacío
                try:
                    # Validar formato de fecha
                    datetime.strptime(self.fecha_ingreso, "%d/%m/%Y")
                    break
                except ValueError:
                    print("Error: Formato de fecha incorrecto. Use dd/mm/aaaa (ej: 15/03/2022)")
            else:
                print("Error: La fecha no puede estar vacía")

        # Validar sueldo (número decimal positivo)
        while True:
            try:
                sueldo_input = input("Sueldo: ").strip()
                if sueldo_input:  # Verificar que no esté vacío
                    self.sueldo = float(sueldo_input)
                    if self.sueldo >= 0:
                        break
                    else:
                        print("Error: El sueldo debe ser mayor o igual a 0")
                else:
                    print("Error: El sueldo no puede estar vacío")
            except ValueError:
                print("Error: Ingrese un número válido para el sueldo")

    def calcular_meses_trabajando(self):
        try:
            print(f"Calculando meses para fecha: {self.fecha_ingreso}")

            # Convertir string a objeto fecha
            fecha_ingreso = datetime.strptime(self.fecha_ingreso, "%d/%m/%Y").date()
            fecha_actual = date.today()

            print(f"Fecha de ingreso: {fecha_ingreso}")
            print(f"Fecha actual: {fecha_actual}")

            # Calcular diferencia en meses
            meses_totales = (fecha_actual.year - fecha_ingreso.year) * 12 + (fecha_actual.month - fecha_ingreso.month)

            print(f"Cálculo base: {meses_totales} meses")

            # Ajustar si el día actual es menor al día de ingreso
            if fecha_actual.day < fecha_ingreso.day:
                meses_totales -= 1
                print(f"Ajuste por días: -1 mes")

            resultado = max(0, meses_totales)
            print(f"Meses finales: {resultado}")

            return resultado

        except Exception as e:
            print(f"Error en cálculo de meses: {e}")
            return 0


class PersonaPrestamo(Persona):
    def __init__(self, nombre="", edad=0, fecha_ingreso="", sueldo=0):
        super().__init__(nombre, edad, fecha_ingreso, sueldo)
        self.aprobado_prestamo = False
        self.cantidad_prestamo = 0

    def verificar_apto_prestamo(self):
        meses_trabajando = self.calcular_meses_trabajando()
        cumple_meses = meses_trabajando > 12
        cumple_edad = self.edad > 25
        print("\n" + "=" * 50)
        print("VERIFICACIÓN DE APTITUD PARA PRÉSTAMO")
        print("=" * 50)
        print(f"Meses trabajando: {meses_trabajando} {'✅' if cumple_meses else '❌'}")
        print(f"Edad: {self.edad} años {'✅' if cumple_edad else '❌'}")
        if cumple_meses and cumple_edad:
            print("\n ¡ESTÁ APTO PARA PRÉSTAMO!")
            self.aprobado_prestamo = True
            return True
        else:
            print("\n NO ESTÁ APTO PARA PRÉSTAMO")
            if not cumple_meses:
                print(f"   - Necesita más de 12 meses trabajando (actual: {meses_trabajando})")
            if not cumple_edad:
                print(f"   - Necesita más de 25 años (actual: {self.edad})")
            self.aprobado_prestamo = False
            return False

    def calcular_prestamo(self):
        if not self.aprobado_prestamo:
            print("\n No se puede calcular préstamo - Persona no apta")
            return 0
        self.cantidad_prestamo = self.sueldo * 10
        print("\n" + "=" * 50)
        print("          DETALLE DE PRÉSTAMO APROBADO")
        print("=" * 50)
        print(f"Sueldo base: S/. {self.sueldo:,.2f}")
        print(f"Préstamo aprobado (10x sueldo): S/. {self.cantidad_prestamo:,.2f}")
        print("=" * 50)
        return self.cantidad_prestamo

    def mostrar_resultado_prestamo(self):
        print("\n" + "★" * 60)
        print("                 RESULTADO FINAL DE PRÉSTAMO")
        print("★" * 60)
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Meses trabajando: {self.calcular_meses_trabajando()} meses")
        print(f"Sueldo: S/. {self.sueldo:,.2f}")
        apto = self.verificar_apto_prestamo()
        if apto:
            prestamo = self.calcular_prestamo()
            print(f"\n ¡FELICIDADES!")
            print(f"Estás aprobado para recibir un préstamo de:")
            print(f"S/. {prestamo:,.2f}")
            print(f"\nDetalle: 10 veces tu sueldo de S/. {self.sueldo:,.2f}")
        else:
            print(f"\n Lo sentimos, no cumples con los requisitos para el préstamo")
        print("★" * 60)


if __name__ == "__main__":
    print("SISTEMA DE PRÉSTAMOS PERSONALES")
    print("=" * 40)
    print("Requisitos para préstamo:")
    print("  - Más de 12 meses trabajando")
    print("  - Edad mayor a 25 años")
    print("  - Préstamo: 10 veces el sueldo actual")
    print("=" * 40)
    personas_prestamo = []
    for i in range(3):
        print(f"\n{'#' * 50}")
        print(f"SOLICITANTE DE PRÉSTAMO {i + 1}")
        print(f"{'#' * 50}")
        persona = PersonaPrestamo()
        persona.inicializar_datos()
        personas_prestamo.append(persona)
    print("\n" + "=" * 70)
    print("                 PROCESANDO SOLICITUDES DE PRÉSTAMO")
    print("=" * 70)
    resultados = []
    for i, persona in enumerate(personas_prestamo, 1):
        print(f"\n--- Solicitante {i}: {persona.nombre} ---")
        persona.mostrar_resultado_prestamo()
        resultados.append({'nombre': persona.nombre, 'aprobado': persona.aprobado_prestamo,
                           'prestamo': persona.cantidad_prestamo if persona.aprobado_prestamo else 0})
    print("\n" + "=" * 70)
    print("                 RESUMEN GENERAL DE PRÉSTAMOS")
    print("=" * 70)
    total_solicitantes = len(resultados)
    aprobados = sum(1 for r in resultados if r['aprobado'])
    rechazados = total_solicitantes - aprobados
    total_prestamos = sum(r['prestamo'] for r in resultados)
    print(f"Total de solicitantes: {total_solicitantes}")
    print(f"Préstamos aprobados: {aprobados}")
    print(f"Préstamos rechazados: {rechazados}")
    print(f"Monto total aprobado: S/. {total_prestamos:,.2f}")
    print("\n--- DETALLES POR SOLICITANTE ---")
    for i, resultado in enumerate(resultados, 1):
        estado = "APROBADO" if resultado['aprobado'] else "RECHAZADO"
        monto = f"S/. {resultado['prestamo']:,.2f}" if resultado['aprobado'] else "S/. 0.00"
        print(f"{i}. {resultado['nombre']}: {estado} - {monto}")
    print("\n" + "=" * 70)
