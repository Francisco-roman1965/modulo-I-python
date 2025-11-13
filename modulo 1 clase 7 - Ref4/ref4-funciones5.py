"""Crear una función que aceptará por parámetro dos valores que serán
ingresados por el usuario, una lista donde los valores serán llenados por el
usuario también y un segundo parámetro que eliminará de la lista que fue
ingresada a la función, finalmente el output de la función será la lista
actualizada sin el valor que se sacará de la lista. Mostrar también la lista
original y el número que fue eliminado."""

print("=== ELIMINADOR DE ELEMENTO DE LISTA ===")


def eliminar_elemento(lista, elemento):
    """
    Función que elimina un elemento de la lista
    Parámetros: lista y elemento a eliminar
    Retorna: lista actualizada
    """
    # Mostrar lista original y elemento a eliminar
    print(f"Lista original: {lista}")
    print(f"Elemento a eliminar: {elemento}")

    # Eliminar el elemento si existe
    if elemento in lista:
        lista.remove(elemento)
        print(f"Elemento '{elemento}' eliminado exitosamente")
    else:
        print(f"El elemento '{elemento}' no existe en la lista")

    return lista


# Solicitar valores al usuario
print("Ingrese los elementos de la lista (separados por comas):")
entrada_lista = input("Lista: ").strip()
lista_usuario = [elemento.strip() for elemento in entrada_lista.split(',') if elemento.strip()]

print("\nIngrese el elemento que desea eliminar:")
elemento_eliminar = input("Elemento: ").strip()

# Usar la función
lista_actualizada = eliminar_elemento(lista_usuario, elemento_eliminar)

# Mostrar output final
print(f"\nLista actualizada: {lista_actualizada}")