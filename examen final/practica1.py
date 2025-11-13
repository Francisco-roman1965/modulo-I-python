"""Escriba un programa donde tendrá los siguientes requisitos (4 ptos):
Reglas:
• Clase base Persona
o Atributos: nombre, edad, nacionalidad="peruana", saldo=0.0.
o Métodos para esta clase:
▪ actualizar_nombre(nombre) y actualizar_edad(edad)
(validar edad > 0).
▪ cumplir_años() (incrementa edad en 1).
▪ mostrar_saldo() (imprime el saldo actual).
▪ transferir(destino, monto) (si no hay fondos
suficientes, imprimir “Saldo insuficiente”; si hay,
basarse en self y acreditar a destino).
• Crear la clase que hereda: Empleado(Persona)
o Atributo adicional: sueldo (float).
o Métodos para esta clase:
▪ aumento_sueldo(porcentaje=0.30) (incrementa el
sueldo en 30% por defecto).
▪ prediccion(año_objetivo, edad_param=None)
▪ Retorna el mensaje: “En el año XXXX tendrá
XX años”.
▪ Si edad_param se pasa y es menor que
self.edad, imprimir “No es posible realizar la
operación” y no calcular.

• Pruebas mínimas
o Instanciar al menos dos Empleado.
o Aplicar aumento_sueldo 2 veces y mostrar el sueldo
incrementado.
o Realizar una transferencia entre ambos empleados y mostrar
saldos antes y después de ambos

o Probar un caso de saldo insuficiente.
o Usar prediccion(...) con y sin edad_param inválido."""


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = "peruana"
        self.saldo = 0.0

    def actualizar_nombre(self, nombre):
        self.nombre = nombre

    def actualizar_edad(self, edad):
        if edad > 0:
            self.edad = edad
        else:
            print("Edad debe ser mayor a 0")

    def cumplir_años(self):
        self.edad += 1
        print(f"{self.nombre} ahora tiene {self.edad} años")

    def mostrar_saldo(self):
        print(f"Saldo de {self.nombre}: S/.{self.saldo:.2f}")

    def transferir(self, destino, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            destino.saldo += monto
            print(f"Transferencia exitosa: S/.{monto:.2f} de {self.nombre} a {destino.nombre}")
        else:
            print("Saldo insuficiente")


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def aumento_sueldo(self, porcentaje=0.30):
        aumento = self.sueldo * porcentaje
        self.sueldo += aumento
        print(f"Aumento del {porcentaje * 100}% aplicado. Nuevo sueldo: S/.{self.sueldo:.2f}")

    def prediccion(self, año_objetivo, edad_param=None):
        if edad_param and edad_param < self.edad:
            print("No es posible realizar la operación")
            return

        años_futuro = año_objetivo - 2024
        edad_futura = self.edad + años_futuro
        return f"En el año {año_objetivo} tendrá {edad_futura} años"


# Probando todo
print("=== CREANDO EMPLEADOS ===")
emp1 = Empleado("Ana", 25, 3000)
emp2 = Empleado("Carlos", 30, 3500)

print(f"\n--- Saldos iniciales ---")
emp1.mostrar_saldo()
emp2.mostrar_saldo()

print(f"\n--- Aumentos de sueldo ---")
emp1.aumento_sueldo()
emp1.aumento_sueldo(0.10)

emp2.aumento_sueldo(0.25)

print(f"\n--- Transferencias ---")
# Dar algo de saldo primero
emp1.saldo = 1000
emp2.saldo = 500

print("Antes de transferir:")
emp1.mostrar_saldo()
emp2.mostrar_saldo()

emp1.transferir(emp2, 300)

print("Después de transferir:")
emp1.mostrar_saldo()
emp2.mostrar_saldo()

print(f"\n--- Caso saldo insuficiente ---")
emp1.transferir(emp2, 1000)

print(f"\n--- Predicciones de edad ---")
print(emp1.prediccion(2030))
print(emp2.prediccion(2035))

print(f"\n--- Predicción con edad inválida ---")
emp1.prediccion(2030, 20)

print(f"\n--- Cumplir años ---")
emp1.cumplir_años()
emp2.cumplir_años()

print(f"\n--- Estado final ---")
emp1.mostrar_saldo()
emp2.mostrar_saldo()
print(f"Sueldo {emp1.nombre}: S/.{emp1.sueldo:.2f}")
print(f"Sueldo {emp2.nombre}: S/.{emp2.sueldo:.2f}")