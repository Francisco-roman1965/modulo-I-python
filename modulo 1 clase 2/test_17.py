"""Hora de entrega máxima: 6 pm
Correo: docente.cerseu.unmsm@gmail.com
Asunto: Ejercicio Participación - Semana 02 - A Práctica 01
Adjuntar archivo .py y screemshot de su respuesta en la terminal
En la parte superior dejar su nombre y apellido: como comentario

Requisitos:
1. Crear 2 variables enteras, 2 variables flotantes, 2 variables string, 1 variable string que contiene valor numérico y una variable boolean
2. Obtener y mostrar la suma de una variable entera con la variable string numérica. (Conversión, realizarla si fuera necesario)
3. Obtener y mostrar la suma de las 2 variables enteras más la variable string numérica y la variable flotante
4. Obtener y mostrar el módulo de las variables enteras: %
5. Obtener y mostrar el resultado de la parte entera de los variables enteras: //
6. Obtener una potencia usando una de las variables flotantes y la variable entera como potencia

Nota: Las variables string pueden ser tu nombre y apellido"""

var_1 = -35
var_2 = 150
var_3 = 15.429
var_4 = -20.87528
nombre = "francisco"
apellido = "román"
dni = "33344455"
var_8 = True

print(nombre, apellido)

suma_1 = int(dni) + var_2
print(suma_1)

suma_2 = int(dni) + var_1 + var_2 + var_3
print(suma_2)

var_2 % var_1
print(var_2 % var_1)

var_2 // var_1
print(var_2 // var_1)

pow(var_3, var_1)
print(var_3 ** var_1)