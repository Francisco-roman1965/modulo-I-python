"""Haciendo el uso de *args y **kwargs aplicarlo debidamente para decorar una función que recibirá 6 argumentos los cuales se multiplicarán entre ellos (3 de ellos serán usado con **kwargs) Mensaje previo al usar el decorador “Está por ejecutarse la función” y mensaje luego de usar el decorador “La función ha sido ejecutado correctamente”
Usar la función decorada al menos 3 veces"""

def decorador_multiplicacion(funcion):
    def wrapper(*args, **kwargs):
        print("Está por ejecutarse la función")
        resultado = funcion(*args, **kwargs)
        print("La función ha sido ejecutada correctamente")
        return resultado
    return wrapper

@decorador_multiplicacion
def multiplicar_numeros(a, b, c, x=1, y=1, z=1):
    resultado = a * b * c * x * y * z
    print(f"Multiplicación: {a} * {b} * {c} * {x} * {y} * {z} = {resultado}")
    return resultado

# Usar la función decorada 3 veces
print("=== PRIMERA EJECUCIÓN ===")
multiplicar_numeros(2, 3, 4, x=5, y=6, z=7)

print("\n=== SEGUNDA EJECUCIÓN ===")
multiplicar_numeros(1, 2, 3, y=4, z=5)

print("\n=== TERCERA EJECUCIÓN ===")
multiplicar_numeros(10, 2, 1, x=3, z=2)