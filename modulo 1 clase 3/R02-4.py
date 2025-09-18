"""4. Hallar el volumen de una esfera, cada dato requerido para hallar el volumen debe estar en una variable. Mostrar el volumen por pantalla
indicándoselo al usuario. Considera a π = 3.14159 La fórmula para calcular el volumen de una esfera es: V = (4/3). π . r ^3 Y finalmente deberá verse lo siguiente:
Radio de la esfera: 5.5 Volumen de la esfera: 696.91"""

pi = 3.14159
radio = 5.5
"""Calcular el volumen usando la fórmula V = (4/3) * π * r³"""
volumen = (4/3) * pi * (radio ** 3)

print("Radio de la esfera:", radio)
print("Volumen de la esfera:", round(volumen, 2))