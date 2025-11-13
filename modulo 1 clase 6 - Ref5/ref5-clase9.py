"""Escribir una clase Figura que debe tener un atributo de nombre de la figura.
Habrá otra clase llamada Rectangulo que hereda de Figura. Pedirá una base y una altura en sus parámetros. Tendrá un método que devuelva el área y perímetro de este rectángulo.
También habrá otra clase llamada Circulo que hereda también de Figura, pedirá por parámetro el radio y este tendrá los métodos que calculará el área y otro método que calculará el perímetro del círculo
Realizar la instancia de la clase figura mínimo 4 veces para mostrar el uso en ambas figuras (2 casos para ambas figuras) y resultados de todos los métodos mediante consola."""

import math

class Figura:
    def __init__(self, nombre): self.nombre = nombre

class Rectangulo(Figura):
    def __init__(self, nombre, base, altura):
        super().__init__(nombre); self.base = base; self.altura = altura
    def area(self): return self.base * self.altura
    def perimetro(self): return 2 * (self.base + self.altura)

class Circulo(Figura):
    def __init__(self, nombre, radio):
        super().__init__(nombre); self.radio = radio
    def area(self): return math.pi * self.radio ** 2
    def perimetro(self): return 2 * math.pi * self.radio

figuras = [Rectangulo("Rectángulo A", 5, 3), Rectangulo("Rectángulo B", 8, 4),
           Circulo("Círculo A", 7), Circulo("Círculo B", 5)]
for f in figuras: print(f"{f.nombre}: Área = {f.area():.2f}, Perímetro = {f.perimetro():.2f}")