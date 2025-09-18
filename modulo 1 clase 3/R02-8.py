"""8. Usando la condicional if imprimir por pantalla si una lista ([]) está vacía o
no, comprobar con una lista vacía y otra con una lista con dato al menos
([dato_1, dato_2])."""

"Verificar si una lista está vacía o no"
"Lista vacía"
lista_vacia = []

"Lista con datos"
lista_con_datos = ["dato_1", "dato_2"]

"Verificar lista vacía"
print("Verificando lista vacía:")
if not lista_vacia:  # Esto es equivalente a if len(lista_vacia) == 0:
    print("La lista está vacía")
else:
    print("La lista NO está vacía")
    print(f"Contenido: {lista_vacia}")

print("\n" + "-"*40 + "\n")

"Verificar lista con datos"
print("Verificando lista con datos:")
if lista_con_datos:  # Esto es equivalente a if len(lista_con_datos) > 0:
    print("La lista NO está vacía")
    print(f"Contenido: {lista_con_datos}")
else:
    print("La lista está vacía")

print("\n" + "-"*40 + "\n")