"""1. Usando los tipos de datos y sus conversiones realizar lo siguiente. (4 ptos)
Reglas:
- Asignar en variables los datos de tu nombre, salario, edad y compañía para un usuario e identificar sus tipos de variables
- Edad tiene que ser tipo string, para usarla más adelante tiene que aplicarse una conversión de datos
- Identificar si la edad es mayor a 30, mostrar un mensaje ingresado “Usted tiene un bono de 10% en el mes de diciembre” caso contrario mostrar “Usted tiene un bono del 5% en el mes diciembre”
- Mostrar el bono final que es: potencia de 2 del salario más el 5 o 10 % de su salario, según corresponda."""

"Asignación de variables con sus respectivos tipos"
nombre = "Francisco Roman Ferreyra"
salario = 4500.00
edad = "59"
compañia = "FORIN APP SAC"

"Identificación de tipos de variables"
print("Tipos de variables:")
print(f"Nombre: {type(nombre)}")
print(f"Salario: {type(salario)}")
print(f"Edad: {type(edad)}")
print(f"Compañía: {type(compañia)}")
print()

"Conversión de edad de string a entero para poder comparar"
edad_int = int(edad)

"Verificación si la edad es mayor a 30"
if edad_int > 30:
    mensaje = "Usted tiene un bono de 10% en el mes de diciembre"
    porcentaje_bono = 0.10
else:
    mensaje = "Usted tiene un bono del 5% en el mes diciembre"
    porcentaje_bono = 0.05

print(mensaje)
print()

"Cálculo del bono final: potencia de 2 del salario más el porcentaje correspondiente"
potencia_salario = salario ** 2
bono_porcentaje = salario * porcentaje_bono
bono_final = potencia_salario + bono_porcentaje

print(f"Salario base: ${salario:.2f}")
print(f"Potencia de 2 del salario: ${potencia_salario:.2f}")
print(f"Bono por porcentaje ({porcentaje_bono*100}%): ${bono_porcentaje:.2f}")
print(f"Bono final: ${bono_final:.2f}")