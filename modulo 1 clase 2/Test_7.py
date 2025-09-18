"crear 4 variables, enteros bolean y str"
"realizar el uso de condicionales de las variables, para 3 condicionales true y dos false"
"3. en caso que valide true, imprimir el caso de las otras dos variables"
"4. entre dos condicionales compara entre dos variable (<>)"

var_1 = 15.429
var_2 = -20.87528

print("El valor de var_1 es: {} y el valor de mi var_2 es: {}".format(var_1, var_2))
print("El valor de mi variable var 2 modificado con 2 decimales".format(f"{var_2:.2f}"))

var_3 = True
var_4 = False
nombre = "python"

print("El valor de var_1: {}".format(var_1))
print("El valor de var_2: {}".format(var_2))

if var_3:
    print("Ingresó a la primera condicional")
    print("Usemos nuestra variable sabiamente")
    print("El valor de var_2: {}".format(var_2))
if var_4:
    print("Ingresó a la segunda condicional")
    print("Usemos nuestra variable sabiamente")
    print("El valor de var_1: {}".format(var_1))
if var_3:
    print("Ingreso a la tercera condicional".format(f"{var_1:.1f}"))
    print("mis variables son: {} {} {}".format(var_1, var_2, var_4))
if var_4:
    print("Ingresó a la cuarta condicional".format(f"{var_2:.2f}"))
    print("mis variables son: {} {} {}".format(var_2, var_3, nombre))
if var_1 < var_2:
    print("¡¡Ingresó a la quinta condicional!!")

