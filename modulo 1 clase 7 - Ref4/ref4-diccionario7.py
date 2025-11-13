"""Realizar un programa donde se ingresarán por consola los nombres de los
alumnos (indicar previamente la cantidad de alumnos a ingresar) de un curso y
las notas de c/u. Guardarás la información en un diccionario donde las claves
serán los nombres de c/u de estos alumnos y sus valores serán las notas de
esto alumnos.
Finalmente mostrarás los alumnos con sus notas en un mensaje similar a
“Pedro tiene la nota de 15” y también la media de todas las notas."""

print("=== REGISTRO DE NOTAS ===")

# Ingresar cantidad de alumnos
try:
    n = int(input("Cantidad de alumnos: "))
except ValueError:
    print("Error: Ingrese un número válido.")
    exit()

# Diccionario para alumnos y notas
alumnos = {}

# Registrar alumnos
for i in range(n):
    print(f"\nAlumno {i + 1}:")
    nombre = input("Nombre: ").strip()

    # Validar que el nombre no esté repetido
    if nombre in alumnos:
        print("¡Alumno ya existe! Ingrese otro nombre.")
        continue

    try:
        nota = float(input("Nota (0-20): "))
        if 0 <= nota <= 20:
            alumnos[nombre] = nota
        else:
            print("Nota fuera de rango. No se registró.")
    except ValueError:
        print("Nota inválida. No se registró.")

# Mostrar resultados
print("\n" + "=" * 40)
print("REPORTE DE NOTAS")
print("=" * 40)

# Mostrar alumnos y notas
for nombre, nota in alumnos.items():
    print(f"→ {nombre} tiene la nota de {nota}")

# Calcular media si hay alumnos
if alumnos:
    promedio = sum(alumnos.values()) / len(alumnos)
    print(f"\nPromedio del curso: {promedio:.2f}")
else:
    print("\nNo hay alumnos registrados.")