anaqueles_revisados = input("liste los anaqueles que ha revisado: ").split(',')
anaqueles_pendientes = list(range(1, 31))
i = 0

while i < len(anaqueles_revisados):
    anaquel = int(anaqueles_revisados[i].strip())
    while anaquel in anaqueles_pendientes:
        anaqueles_pendientes.remove(anaquel)
    i += 1

print("Anaqueles pendientes:", ', '.join(map(str, anaqueles_pendientes)))
