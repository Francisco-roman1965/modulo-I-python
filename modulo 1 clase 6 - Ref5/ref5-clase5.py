"""Crear una clase Persona con los siguientes requerimientos. La clase tendrá como atributos el nombre, edad y sueldo de una persona. Implementar los métodos necesarios para inicializar los atributos (constructor), un método para mostrar los datos e indicar si la persona es mayor de edad o no y otro método que bonificación que retornará el 20% adicional de su sueldo, en caso sea mayor de edad. Un método para saber cuántos meses ha estado trabajando en la empresa. Instanciar por lo menos la clase con 3 diferentes personas."""

class Persona:
    def __init__(self, nombre="", edad=0, fecha_ingreso="", sueldo=0):
        self.nombre = nombre
        self.edad = edad
        self.fecha_ingreso = fecha_ingreso
        self.sueldo = sueldo

    def inicializar_datos(self):
        self.nombre = input("Nombre: ")
        self.edad = int(input("Edad: "))
        self.fecha_ingreso = input("Fecha ingreso (dd/mm/aaaa): ")
        self.sueldo = float(input("Sueldo: "))

    def es_mayor_edad(self):
        return self.edad >= 18

    def calcular_bonificacion(self):
        if self.es_mayor_edad():
            return self.sueldo * 0.20
        return 0

    def calcular_meses_trabajando(self):
        try:
            # Dividir la fecha en día, mes y año
            dia_ing, mes_ing, año_ing = map(int, self.fecha_ingreso.split('/'))

            # Obtener fecha actual (forma básica)
            from datetime import date
            hoy = date.today()
            dia_act = hoy.day
            mes_act = hoy.month
            año_act = hoy.year

            # Calcular meses trabajados
            meses_totales = (año_act - año_ing) * 12 + (mes_act - mes_ing)

            # Ajustar si el día actual es menor al día de ingreso
            if dia_act < dia_ing:
                meses_totales -= 1

            return max(0, meses_totales)

        except Exception as e:
            print(f"Error al calcular meses: {e}")
            return 0

    def mostrar_datos(self):
        print(f"\nNombre: {self.nombre}")
        print(f"Edad: {self.edad} - {'Mayor' if self.es_mayor_edad() else 'Menor'} de edad")
        print(f"Meses trabajando: {self.calcular_meses_trabajando()}")
        print(f"Sueldo: S/. {self.sueldo:.2f}")
        if self.es_mayor_edad():
            print(f"Bonificación: S/. {self.calcular_bonificacion():.2f}")
            print(f"Total: S/. {self.sueldo + self.calcular_bonificacion():.2f}")


# Uso simplificado
if __name__ == "__main__":
    personas = []

    for i in range(3):
        print(f"\nPersona {i + 1}:")
        p = Persona()
        p.inicializar_datos()
        personas.append(p)

    for p in personas:
        p.mostrar_datos()
