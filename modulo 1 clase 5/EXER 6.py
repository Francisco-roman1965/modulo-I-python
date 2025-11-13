"""Crear diccionario de contactos, el cual tendrá como key: Nombre, value: teléfono (9 dígitos)
- Verificar si existe el número de contacto de una persona, para esto estos valores serán
verificados con variables, entre 2 que existan y dos que no existan
- Indicar mediante un mensaje si está o no agregados a la agenda de contactos
- En caso que no exista agregarlo al diccionario de contactos
- Mostrar finalmente el diccionario actualizado."""

# Diccionario de contactos inicial# Diccionario inicial y contactos a verificar
agenda = {"Juan Pérez": "987654321", "María García": "912345678", "Carlos López": "934567890"}
contactos = [("Juan Pérez", "987654321"), ("María García", "912345678"), ("Laura Rodríguez", "978654321"), ("Pedro Sánchez", "923456789")]

# Proceso principal con un solo for
for nombre, telefono in contactos:
    print(f"\nVerificando: {nombre}")
    if nombre in agenda:
        print(f"✅ Ya existe: {agenda[nombre]}")
    else:
        agenda[nombre] = telefono
        print(f"✅ Agregado: {telefono}")

# Mostrar agenda actualizada
print(f"\n📞 Agenda final: {agenda}")