"""Requisitos:
- Crear dos listas vacías
- Agregar los datos de nombre, apellido paterno, edad y profesión para ambas listas
- Obtener y mostrar la suma de las edades de ambas listas
- Sumar las listas y mostrar el resultado en la terminal
- Mostrar de forma inversa la suma de ambas listas
- Actualizar la nueva lista eliminando la edad de la primera y el apellido del segundo
(Utilizar cualquiera de los métodos de eliminación)"""

def main():

    "1. Crear dos listas vacías"
    lista1 = []
    lista2 = []

    print("=== LISTAS INICIALES ===")
    print(f"Lista 1: {lista1}")
    print(f"Lista 2: {lista2}")
    print()

    "2. Agregar datos a ambas listas"
    "Lista 1: Datos de persona 1"
    lista1.append("Juan")
    lista1.append("Pérez")
    lista1.append(25)
    lista1.append("Ingeniero")

    "Lista 2: Datos de persona 2"
    lista2.append("María")
    lista2.append("Gómez")
    lista2.append(30)
    lista2.append("Doctora")

    print("=== LISTAS CON DATOS ===")
    print(f"Lista 1: {lista1}")
    print(f"Lista 2: {lista2}")
    print()

    "3. Obtener y mostrar suma de edades"
    edad_lista1 = lista1[2]
    edad_lista2 = lista2[2]
    suma_edades = edad_lista1 + edad_lista2

    print("=== SUMA DE EDADES ===")
    print(f"Edad lista 1: {edad_lista1} años")
    print(f"Edad lista 2: {edad_lista2} años")
    print(f"Suma total: {suma_edades} años")
    print()

    "4. Sumar las listas y mostrar resultado"
    lista_suma = lista1 + lista2

    print("=== SUMA DE LISTAS ===")
    print(f"Lista 1 + Lista 2 = {lista_suma}")
    print()

    "5. Mostrar de forma inversa la suma de ambas listas"
    lista_inversa = lista_suma[::-1]

    print("=== LISTA INVERSA ===")
    print(f"Lista invertida: {lista_inversa}")
    print()

    "6. Actualizar nueva lista eliminando elementos"
    "Crear copia para no modificar la original"
    lista_actualizada = lista_suma.copy()

    "Eliminar edad de la primera persona (índice 2)"
    "Eliminar apellido del segundo (índice 5 porque: lista1[0-3] + lista2[0-3])"
    "lista_suma = ['Juan', 'Pérez', 25, 'Ingeniero', 'María', 'Gómez', 30, 'Doctora']"
    "Índices:       0       1       2       3         4        5       6       7"

    "Método 1: del por índice"
    del lista_actualizada[2]

    "Método 2: remove por valor (asumiendo que 'Gómez' es único en la lista)"
    if 'Gómez' in lista_actualizada:
        lista_actualizada.remove('Gómez')

    print("=== LISTA ACTUALIZADA ===")
    print("Eliminados: edad primera persona y apellido segunda persona")
    print(f"Lista actualizada: {lista_actualizada}")
    print()

    "Mostrar información estructurada"
    print("=== RESUMEN FINAL ===")
    print(f"Lista 1 original: {lista1}")
    print(f"Lista 2 original: {lista2}")
    print(f"Suma listas: {lista_suma}")
    print(f"Lista invertida: {lista_inversa}")
    print(f"Lista actualizada: {lista_actualizada}")

if __name__ == "__main__":
    main()