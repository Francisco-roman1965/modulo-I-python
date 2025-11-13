"""Crear un decorador conteo_parametros(funcion) donde imprimirá la cantidad de argumentos que tiene la función a decorar usando *args y
**kwargs.
Mensaje previo “La cantidad de argumentos que tiene la función es” mensaje post “La función decoradora terminó de ejecutarse correctamente”
Ejemplo: Al usar una función suma que creamos: suma(4, 1, 10, 2, 50, 64)
Salida:
“La cantidad de argumentos que tiene la función es 5”
“La función decoradora terminó de ejecutarse correctamente”
Consideración:
Todos los parámetros ingresados deben ser enteros, caso sean String alguno de ellos indicar al usuario: “Solo está admitido datos enteros, no se podrá realizar la suma”
Usar la función al menos 3 veces"""


def conteo_parametros(func):
    def wrapper(*args, **kwargs):
        todos_enteros = all(isinstance(arg, int) for arg in args) and all(isinstance(v, int) for v in kwargs.values())
        if not todos_enteros: print("Solo está admitido datos enteros, no se podrá realizar la suma"); return None

        total_args = len(args) + len(kwargs)
        print(f"La cantidad de argumentos que tiene la función es {total_args}")
        resultado = func(*args, **kwargs)
        print("La función decoradora terminó de ejecutarse correctamente")
        return resultado

    return wrapper


@conteo_parametros
def suma(*args, **kwargs):
    total = sum(args) + sum(kwargs.values())
    print(f"Resultado: {total}")
    return total


# 3 ejecuciones
print("=== EJECUCIÓN 1 ===");
suma(4, 1, 10, 2, 50, 64)
print("\n=== EJECUCIÓN 2 ===");
suma(5, 10, 15, x=20, y=25)
print("\n=== EJECUCIÓN 3 ===");
suma(1, 2, "3", 4)