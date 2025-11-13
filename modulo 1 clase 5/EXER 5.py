"""Listas en python"""

"""
Lista: Recorrido de las listas en un búcle for
"""

notas = [12, 18, 16, 20, 11, 14, 13]

i = 0
for nota in notas:
    #print(nota)
    #print("Nota: {}".format(nota))
    #print(notas[i])
    #notas[i] = nota - 2
    #print("Nota actualizada: {}".format(notas[i]))
    #i = i + 1

    #print(notas)

    #notas [i] = nota + 3
    #print("Nota actualizada: {}".format(notas[i]))

    notas[i] = nota/2
    print("Nota actualizada: {}".format(notas[i]))