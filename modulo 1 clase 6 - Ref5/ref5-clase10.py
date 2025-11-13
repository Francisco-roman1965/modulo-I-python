"""Crear una clase llamada Soldado para un juego sobre un mapa la cual deberá tener como atributos en el constructor posición X y posición Y las cuales iniciarán en 0, agregar un nombre a este soldado dentro de estos atributos.
La clase debe tener los siguientes métodos. Caminar hacia el eje X en donde se indicará cuántos pasos dará y otra clase que le permitirá caminar por el eje Y, en caso se indique un número negativo indicar que solo puede llegar hasta el 0 si es menor a los pasos ya dados.
Crear finalmente un método adicional que irá guardando los pasos que ha dado dentro de una lista para que finalmente al usar este método me muestre el historial de movimientos del Soldado, tanto en el eje X y en eje Y
Instanciar un mínimo de 5 movimientos para que muestre finalmente el historial de pasos de tu soldado"""


class Soldado:
    def __init__(self, nombre):
        self.nombre = nombre
        self.x = 0
        self.y = 0
        self.historial = []

    def caminar_x(self, pasos):
        nuevo_x = max(0, self.x + pasos)
        self.historial.append(f"Eje X: {self.x} → {nuevo_x}")
        self.x = nuevo_x

    def caminar_y(self, pasos):
        nuevo_y = max(0, self.y + pasos)
        self.historial.append(f"Eje Y: {self.y} → {nuevo_y}")
        self.y = nuevo_y

    def mostrar_historial(self):
        print(f"\nHistorial de movimientos - {self.nombre}:")
        [print(f"  {mov}") for mov in self.historial]


soldado = Soldado("Comandante Rex")
soldado.caminar_x(5)
soldado.caminar_y(3)
soldado.caminar_x(-2)
soldado.caminar_y(-1)
soldado.caminar_x(3)
soldado.caminar_y(4)
soldado.mostrar_historial()