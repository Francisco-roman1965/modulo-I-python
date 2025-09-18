"""11. Identificar qué tipo de dato se obtiene al elevar tu edad con
exponente 5 y luego dividirlo por 10. Mostrar el resultado de su módulo con
3 en pantalla"""

# Solicitar la edad al usuario
edad = int(input("Por favor, ingresa tu edad: "))

# Elevar la edad al exponente 5
resultado_exponente = edad ** 5
10
# Dividir el resultado por 10
resultado_division = resultado_exponente / 10

# Calcular el módulo con 3
resultado_modulo = resultado_division % 3

# Mostrar todos los resultados
print(f"\nTu edad: {edad}")
print(f"Edad elevada a la 5: {edad}⁵ = {resultado_exponente}")
print(f"Dividido por 10: {resultado_exponente} / 10 = {resultado_division}")
print(f"Tipo de dato después de la división: {type(resultado_division)}")
print(f"Módulo con 3: {resultado_division} % 3 = {resultado_modulo}")
print(f"Tipo de dato final: {type(resultado_modulo)}")