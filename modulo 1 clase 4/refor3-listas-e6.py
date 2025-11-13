"""Tiene una lista de invitados que llegaron a una boda de acuerdo a su orden
de llegada:
guests = [“Ana”, "Raúl", “Katherine”, “Pedro”, “Raúl”, “Fiorella”, “Miguel”]
Se requiere reorganizar esta lista.
Primero los que tienen número impar y en el orden que fueron llegando
Segundo las personas que tienen número par de letras
Input: [“Ana”, “Raúl”, “Fiorella”, “Katherine”, "Pedro", “Miguel”, “Luis”]
Output: [“Ana”, “Raúl”, ”Katherine”, “Pedro”, “Fiorella”, “Miguel”, “Luis”]"""

def reorganizar_lista_invitados(guests):
    """
    Reorganiza la lista de invitados: primero los que tienen número impar de letras,
    manteniendo el orden de llegada, luego los que tienen número par de letras.

    Args:
        guests (list): Lista original de invitados

    Returns:
        list: Lista reorganizada
    """
    # Separar en dos listas: impares y pares
    impares = []
    pares = []

    for invitado in guests:
        # Contar letras (eliminando espacios si los hubiera)
        cantidad_letras = len(invitado.replace(" ", ""))

        if cantidad_letras % 2 == 1:  # Número impar de letras
            impares.append(invitado)
        else:  # Número par de letras
            pares.append(invitado)

    # Combinar las listas: primero impares, luego pares
    return impares + pares


def main():
    # Lista original de invitados según orden de llegada
    guests = ["Ana", "Raúl", "Katherine", "Pedro", "Luis", "Fiorella", "Miguel"]

    print("=== REORGANIZACIÓN DE LISTA DE INVITADOS ===")
    print(f"Lista original (orden de llegada): {guests}")

    # Reorganizar la lista
    lista_reorganizada = reorganizar_lista_invitados(guests)

    print(f"Lista reorganizada: {lista_reorganizada}")

if __name__ == "__main__":
    main()