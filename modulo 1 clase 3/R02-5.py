"""5. Crear un programa que inicia creando un sueldo en una variable, sepamos si
es par o impar mediante un mensaje. Utilizar módulo y condicional (if)."""

sueldo = 2500

"Verificar si el sueldo es par o impar usando el operador módulo (%)"
if sueldo % 2 == 0:
    print(f"El sueldo de ${sueldo} es PAR")
else:
    print(f"El sueldo de ${sueldo} es IMPAR")