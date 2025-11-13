"""Ingresar por consola el tamaño de una lista, luego empezarás a ingresar los datos mediante consola también (5 compañías relacionadas con al mundo de TI) y harás una copia donde adrede agregarás nombres que estarán repetidos (mediante consola) para que finalmente muestres otra lista donde
solo se mostrará los nombres no repetidos y también te mostrará la lista inicial"""

def main():
    # Solicitar el tamaño de la lista
    while True:
        try:
            tamaño = int(input("Ingrese el tamaño de la lista (mínimo 5): "))
            if tamaño >= 5:
                break
            else:
                print("El tamaño debe ser al menos 5. Intente nuevamente.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

    print(f"\nIngrese {tamaño} compañías relacionadas con TI:")

    # Ingresar las compañías originales
    compañias_originales = []
    for i in range(tamaño):
        while True:
            compañia = input(f"Compañía {i + 1}: ").strip()
            if compañia:
                compañias_originales.append(compañia)
                break
            else:
                print("No puede ingresar un nombre vacío. Intente nuevamente.")

    print("\n" + "=" * 50)
    print("Ahora crearemos una copia y agregaremos nombres repetidos:")

    # Crear copia y agregar elementos repetidos
    compañias_copia = compañias_originales.copy()

    # Solicitar cuántos elementos repetidos agregar
    while True:
        try:
            repetidos = int(input("\n¿Cuántos elementos repetidos desea agregar? "))
            if repetidos >= 0:
                break
            else:
                print("Debe ser un número positivo o cero.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

    # Agregar elementos repetidos
    for i in range(repetidos):
        while True:
            compañia = input(f"Elemento repetido {i + 1}: ").strip()
            if compañia:
                # Verificar si ya existe en la lista original
                if compañia in compañias_originales:
                    compañias_copia.append(compañia)
                    break
                else:
                    print("ADVERTENCIA: Esta compañía no existe en la lista original.")
                    confirmar = input("¿Desea agregarla de todas formas? (s/n): ").lower()
                    if confirmar == 's':
                        compañias_copia.append(compañia)
                        break
            else:
                print("No puede ingresar un nombre vacío.")

    # Obtener lista sin duplicados
    compañias_sin_repetir = list(set(compañias_copia))

    # Mostrar resultados
    print("\n" + "=" * 50)
    print("RESULTADOS FINALES:")
    print("=" * 50)

    print(f"\n📋 Lista inicial ({len(compañias_originales)} elementos):")
    for i, compañia in enumerate(compañias_originales, 1):
        print(f"  {i}. {compañia}")

    print(f"\n📝 Lista con elementos repetidos ({len(compañias_copia)} elementos):")
    for i, compañia in enumerate(compañias_copia, 1):
        print(f"  {i}. {compañia}")

    print(f"\n✅ Lista sin elementos repetidos ({len(compañias_sin_repetir)} elementos):")
    for i, compañia in enumerate(sorted(compañias_sin_repetir), 1):
        print(f"  {i}. {compañia}")

    # Mostrar estadísticas
    print(f"\n📊 Estadísticas:")
    print(f"  - Elementos en lista original: {len(compañias_originales)}")
    print(f"  - Elementos en lista con repetidos: {len(compañias_copia)}")
    print(f"  - Elementos únicos: {len(compañias_sin_repetir)}")
    print(f"  - Elementos repetidos agregados: {repetidos}")


if __name__ == "__main__":
    print("🐍 PROGRAMA DE GESTIÓN DE COMPAÑÍAS TI 🐍")
    print("Este programa maneja listas de compañías de tecnología")
    main()