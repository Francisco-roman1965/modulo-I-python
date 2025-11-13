"""Escribe un programa que convierta cierta cantidad de soles a dólares, usando un tipo de cambio que se proporciona en el programa.
Estos valores estarán dentro de sus variables respectivamente.
La salida mostrará tres cambios que hagas respectivamente de tres montos a convertir."""

# Programa simple de conversión de soles a dólares)

# Definir variables
tipo_cambio = 3.75  # 1 dólar = 3.75 soles

# Tres montos diferentes en soles
monto1_soles = 100.0
monto2_soles = 250.0
monto3_soles = 500.0

# Realizar las conversiones
monto1_dolares = monto1_soles / tipo_cambio
monto2_dolares = monto2_soles / tipo_cambio
monto3_dolares = monto3_soles / tipo_cambio

# Mostrar resultados
print("CONVERSIÓN DE SOLES A DÓLARES")
print("=" * 35)
print(f"Tipo de cambio: 1 USD = {tipo_cambio} PEN")
print("=" * 35)

print(f"Conversión 1: {monto1_soles:,.2f} PEN = {monto1_dolares:,.2f} USD")
print(f"Conversión 2: {monto2_soles:,.2f} PEN = {monto2_dolares:,.2f} USD")
print(f"Conversión 3: {monto3_soles:,.2f} PEN = {monto3_dolares:,.2f} USD")