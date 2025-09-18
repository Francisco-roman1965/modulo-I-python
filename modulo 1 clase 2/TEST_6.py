"""
Requisitos:

1. Crear dos variables para los valores de nombre, profesión y ciudad
2. Crear dos variables para la remuneración de enero y febrero (mayor a 1500)
3. Crear 1 variable donde se sumará el ingreso de los dos meses, enero y febrero
4. Mostrar en pantalla el siguiente mensaje (Output):

"Hola soy 'nombre', soy 'profesión' y mi remuneración acumulada es de 'remunera_total'"

"""
nombre = "francisco"
profesion = "químico"
ciudad = "Lima"

var_1 = 2500
var_2 = 3400

var_3 = var_1 + var_2
print("hola soy {} de profesion {} y mi remuneración acumulada es de {}".format(nombre, profesion, var_3))
