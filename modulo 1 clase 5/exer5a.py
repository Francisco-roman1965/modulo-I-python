"""Listas en python"""

"""
Lista: Recorrido de las listas en un búcle for
"""

notas = [12, 18, 16, 20, 11, 14, 19]


i = 0
for nota in notas:
    notas[i] = nota/2
    print("Nota actualizada: {}".format(notas[i]))
    i = i + 1

notas.insert(8, 12)
notas.insert(9, 19)
print("notas: {}".format(notas))
print("Notas: {}".format(notas[i]))