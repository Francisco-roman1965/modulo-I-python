"""1. Escriba un programa donde tendrá los siguientes requisitos (3 ptos):
Reglas:
- Crear una función llamada procesar_notas(estudiantes) la cual va a recibir
un diccionario donde las claves serán los nombres de los estudiantes y sus
valores serán listas con 3 notas.
- Calcular el promedio de cada estudiante.
- Devolver un nuevo diccionario donde la clave sea el nombre del estudiante
y el valor sea otro diccionario con:
promedio: que será el promedio de notas
estado: “aprobado” si es mayor o igual a 11, “desaprobado” si es menor
- Mostrar en pantalla el estudiante con mayor promedio"""

def procesar_notas(estudiantes):
    """Procesa las notas de los estudiantes y calcula promedios y estados. Args: estudiantes (dict): Diccionario con nombres como clave y listas de 3 notas como valor. Returns: dict: Nuevo diccionario con información procesada de cada estudiante."""

    resultados = {}

    for nombre, notas in estudiantes.items():
        # Calcular el promedio de las 3 notas
        promedio = sum(notas) / len(notas)

        # Determinar el estado según el promedio
        estado = "aprobado" if promedio >= 11 else "desaprobado"

        # Crear el diccionario interno con promedio y estado
        resultados[nombre] = {
            "promedio": round(promedio, 2),  # Redondear a 2 decimales
            "estado": estado
        }

    return resultados

def encontrar_mejor_estudiante(resultados):
    """ Encuentra y muestra al estudiante con el mayor promedio. Args: resultados (dict): Diccionario con los resultados procesados."""

    if not resultados:
        print("No hay estudiantes para evaluar.")
        return

    # Encontrar el estudiante con el mayor promedio
    mejor_estudiante = max(resultados.items(), key=lambda x: x[1]["promedio"])
    nombre = mejor_estudiante[0]
    promedio = mejor_estudiante[1]["promedio"]

    print(f"\n ESTUDIANTE CON MAYOR PROMEDIO:")
    print(f"Nombre: {nombre}")
    print(f"Promedio: {promedio}")
    print(f"Estado: {resultados[nombre]['estado']}")

def mostrar_resultados(resultados):
    """ Muestra los resultados de todos los estudiantes de forma ordenada. Args: resultados (dict): Diccionario con los resultados procesados."""

    print("\n RESULTADOS DE ESTUDIANTES:")
    print("-" * 40)

    for nombre, datos in resultados.items():
        print(f"Estudiante: {nombre}")
        print(f"  Promedio: {datos['promedio']}")
        print(f"  Estado: {datos['estado']}")
        print("-" * 40)

def main():
    """Función principal que ejecuta el programa completo."""
    # Diccionario de ejemplo con estudiantes y sus notas
    estudiantes = {
        "Ana García": [13, 18, 16],
        "Luis Martínez": [10, 12, 9],
        "María López": [18, 16, 19],
        "Carlos Rodríguez": [11, 10, 14],
        "Sofia Torres": [9, 7, 10]
    }

    print("=" * 50)
    print("      SISTEMA DE PROCESAMIENTO DE NOTAS")
    print("=" * 50)

    # Mostrar datos originales
    print("\n DATOS ORIGINALES:")
    for nombre, notas in estudiantes.items():
        print(f"{nombre}: {notas}")

    # Procesar las notas
    resultados = procesar_notas(estudiantes)

    # Mostrar resultados
    mostrar_resultados(resultados)

    # Encontrar y mostrar al mejor estudiante
    encontrar_mejor_estudiante(resultados)

# Ejecutar el programa
if __name__ == "__main__":
    main()