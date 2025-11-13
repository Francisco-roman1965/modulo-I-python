"""Crear una clase llamada Circulo que contenga radio en su constructor y que contenga un método área que devuelva el área de un círculo.
Adicionalmente habrá un método que devuelva el perímetro del círculo. También habrá un método donde pedirá el radio del círculo.
Instanciar mínimo 2 veces la clase y mostrar resultados por consola."""


class Circulo:
    def __init__(self, radio=0):
        """Constructor que inicializa el radio del círculo"""
        self.radio = radio

    def pedir_radio(self):
        """Método para pedir el radio del círculo"""
        self.radio = float(input("Ingrese el radio del círculo: "))

    def area(self):
        """Método que devuelve el área del círculo"""
        return 3.1416 * self.radio ** 2

    def perimetro(self):
        """Método que devuelve el perímetro del círculo"""
        return 2 * 3.1416 * self.radio


# Programa principal simplificado
if __name__ == "__main__":
    print("CALCULADORA DE CÍRCULOS - VERSIÓN SIMPLIFICADA")
    print("=" * 45)

    # Crear dos círculos
    circulo1 = Circulo()
    circulo2 = Circulo()

    # Primer círculo
    print("\n--- PRIMER CÍRCULO ---")
    circulo1.pedir_radio()
    print(f"Radio: {circulo1.radio}")
    print(f"Área: {circulo1.area():.2f}")
    print(f"Perímetro: {circulo1.perimetro():.2f}")

    # Segundo círculo
    print("\n--- SEGUNDO CÍRCULO ---")
    circulo2.pedir_radio()
    print(f"Radio: {circulo2.radio}")
    print(f"Área: {circulo2.area():.2f}")
    print(f"Perímetro: {circulo2.perimetro():.2f}")