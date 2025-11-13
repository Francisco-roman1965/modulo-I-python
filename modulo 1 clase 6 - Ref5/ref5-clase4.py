"""Crear una clase Alumno que tenga como atributos el nombre, edad y la nota final del alumno. Crear los métodos para inicializar sus atributos, otro para imprimirlos y un método para mostrar un mensaje con el resultado de la nota, si ha aprobado (mayor o igual a 13) o no el alumno. Instanciar la clase por lo menos 4 veces (4 alumnos)"""

class Alumno:
    def __init__(self, nombre="", edad=0, nota_final=0):
        self.nombre = nombre
        self.edad = edad
        self.nota_final = nota_final

    def inicializar_datos(self):
        """Método simplificado para ingresar datos"""
        self.nombre = input("Nombre del alumno: ")
        self.edad = int(input("Edad del alumno: "))
        self.nota_final = float(input("Nota final (0-20): "))

    def imprimir_datos(self):
        """Método simplificado para mostrar datos"""
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Nota: {self.nota_final}")

    def mostrar_resultado(self):
        """Método para mostrar si aprobó o no"""
        self.imprimir_datos()
        if self.nota_final >= 13:
            print("Resultado: APROBADO")
        else:
            print("Resultado: DESAPROBADO")


# Programa principal simplificado
if __name__ == "__main__":
    print("SISTEMA DE ALUMNOS - VERSIÓN SIMPLIFICADA")

    # Crear 4 alumnos
    alumnos = []

    for i in range(4):
        print(f"\n--- Alumno {i + 1} ---")
        alumno = Alumno()
        alumno.inicializar_datos()
        alumnos.append(alumno)

    # Mostrar resultados
    print("\n--- RESULTADOS ---")
    for i, alumno in enumerate(alumnos, 1):
        print(f"\nAlumno {i}:")
        alumno.mostrar_resultado()