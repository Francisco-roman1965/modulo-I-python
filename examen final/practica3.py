"""Crear un decorador conteo.
Reglas:
- El decorador retornará la cantidad de parámetros que hayas usado en la
función y que a su vez evaluará que deba ser mayor que 1 para procesar esta
lógica, caso contrario indicarlo con un mensaje respectivamente al usuario.
- Al final de la función decorada indicará mediante un mensaje que la función
fue ejecutada exitosamente.
- La función que vas a crear va a capturar, la edad, nombre de un alumno, la
hora y el minuto en que fue registrado (usar la librería correspondiente de
tiempo)
Mostrando un mensaje siguiente: “Pedro de 30 años ha sido registrado a las
16 horas con 20 minutos”
- La función que será decorada también estará pasando 4 notas que calculará
la media del estudiante."""

import datetime

def conteo(func):
    def wrapper(*args, **kwargs):
        total_parametros = len(args) + len(kwargs)

        if total_parametros <= 1:
            print("Error: Necesitas más de 1 parámetro")
            return None

        print(f"Se usaron {total_parametros} parámetros")
        resultado = func(*args, **kwargs)
        print("Función ejecutada exitosamente")
        return resultado

    return wrapper

@conteo
def registrar_alumno(nombre, edad, nota1, nota2, nota3, nota4):
    ahora = datetime.datetime.now()
    hora = ahora.hour
    minuto = ahora.minute

    promedio = (nota1 + nota2 + nota3 + nota4) / 4

    mensaje = f"{nombre} de {edad} años ha sido registrado a las {hora} horas con {minuto} minutos"
    print(mensaje)
    print(f"Promedio: {promedio:.1f}")

    return promedio

# Probando el decorador
print("=== PRUEBA 1 - Correcta ===")
result1 = registrar_alumno("Pedro", 30, 15, 16, 14, 17)

print("\n=== PRUEBA 2 - Correcta ===")
result2 = registrar_alumno("Maria", 25, 18, 19, 17, 16)

print("\n=== PRUEBA 3 - Con pocos parámetros ===")
# Esto fallará por el decorador
try:
    registrar_alumno("SoloNombre")
except:
    pass

print("\n=== PRUEBA 4 - Otro alumno ===")
result3 = registrar_alumno("Carlos", 22, 12, 13, 14, 15)

print("\n=== RESUMEN ===")
print(f"Pedro: {result1:.1f}")
print(f"Maria: {result2:.1f}")
print(f"Carlos: {result3:.1f}")