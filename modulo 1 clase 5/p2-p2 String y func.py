"""2. Usando el concepto de funciones (3 ptos):
Reglas:
- Crear una función normalizar_nombres(nombres)
- El parámetro recibe una lista de string de nombres (6 como mínimo)
- Este quitará el espacio antes y después si lo hubiera
- Convierte en tipo título
- Si hubiera más nombre los debe separar (si debe haber el caso en el input de
datos)
- Devuelve también eliminando duplicados manteniendo el orden de la primera
- No mutará la lista original"""

def normalizar_nombres(nombres):
    """ Normaliza una lista de nombres: - Elimina espacios al inicio y final - Convierte a formato título - Separa nombres compuestos - Elimina duplicados manteniendo el orden - No muta la lista original, Args: nombres (list): Lista de strings con nombres, Returns: list: Lista normalizada sin duplicados"""

    # Verificar que la lista tenga al menos 6 elementos
    if len(nombres) < 6:
        raise ValueError("La lista debe contener al menos 6 nombres")

    # Crear una copia para no mutar la lista original
    nombres_copia = nombres.copy()
    nombres_normalizados = []
    nombres_unicos = set()

    for nombre in nombres_copia:
        # Eliminar espacios al inicio y final
        nombre_limpio = nombre.strip()

        # Convertir a formato título
        nombre_titulo = nombre_limpio.title()

        # Separar nombres compuestos (si existen)
        nombres_separados = nombre_titulo.split()

        for nombre_sep in nombres_separados:
            # Si el nombre no está en el conjunto de únicos, agregarlo
            if nombre_sep not in nombres_unicos:
                nombres_normalizados.append(nombre_sep)
                nombres_unicos.add(nombre_sep)

    return nombres_normalizados


# Ejemplo de uso y prueba
if __name__ == "__main__":
    # Lista de prueba con más de 6 nombres
    lista_nombres = [
        "  juan perez  ",
        "MARÍA GARCÍA",
        "carlos lopez rodriguez",
        "  ana martinez  ",
        "JUAN PEREZ",  # Duplicado
        "luisa fernández",
        "pedro Sánchez",
        "carlos lopez rodriguez",  # Duplicado
        "  maría garcía  ",  # Duplicado
        "miguel angel ramos"
    ]

    print("Lista original:")
    for i, nombre in enumerate(lista_nombres, 1):
        print(f"{i}. '{nombre}'")

    print("\nLista normalizada:")
    nombres_normalizados = normalizar_nombres(lista_nombres)
    for i, nombre in enumerate(nombres_normalizados, 1):
        print(f"{i}. {nombre}")

    print(f"\n¿La lista original fue modificada? {lista_nombres == lista_nombres}")
    print(f"Lista original: {lista_nombres}")
    print(f"Lista normalizada: {nombres_normalizados}")

    # Prueba con menos de 6 nombres (debe generar error)
    try:
        lista_corta = ["juan", "maria", "carlos"]
        normalizar_nombres(lista_corta)
    except ValueError as e:
        print(f"\nError esperado: {e}")