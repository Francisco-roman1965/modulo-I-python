"""Desarrolla una clase Agenda que administrará contactos. Dentro de una lista se debe almacenar un diccionario para cada contacto el nombre, el teléfono, email y DNI. Deberá tener los siguientes métodos:
Añadir contacto, Mostrar contactos y Buscar contacto (Por DNI) Estructura de la lista cada vez que vas agregando un contacto: contactos = [{‘nombre’: “Luis”, ‘telefono’: “997667945”, ‘email’: “luishh@gmail.com”, ‘dni’: 44234239},
{‘nombre’: “Milagros”, ‘telefono’: “997654687”, ‘email’: “milagros19c@gmail.com”, ‘dni’: 43423211}]. Agregar por lo menos 4 personas (instanciándolas) para poder luego realizar la búsqueda de estas personas en la agenda y saber si existen, en caso contrario indicar: “´Nombre´ no se encuentra anotado en la agenda”"""

class Agenda:
    def __init__(self): self.contactos = []
    def añadir_contacto(self, nombre, telefono, email, dni): self.contactos.append({'nombre': nombre, 'telefono': telefono, 'email': email, 'dni': dni})
    def mostrar_contactos(self):
        for contacto in self.contactos: print(f"Nombre: {contacto['nombre']}, Tel: {contacto['telefono']}, Email: {contacto['email']}, DNI: {contacto['dni']}")
    def buscar_contacto(self, dni):
        for contacto in self.contactos:
            if contacto['dni'] == dni: return contacto
        return f"DNI {dni} no se encuentra en la agenda"

agenda = Agenda()
agenda.añadir_contacto("Luis", "997667945", "luishh@gmail.com", 44234239)
agenda.añadir_contacto("Milagros", "997654687", "milagros19c@gmail.com", 43423211)
agenda.añadir_contacto("Carlos", "987654321", "carlos@email.com", 12345678)
agenda.añadir_contacto("Ana", "912345678", "ana@email.com", 87654321)

print("=== TODOS LOS CONTACTOS ===")
agenda.mostrar_contactos()

print("\n=== BÚSQUEDAS ===")
print(agenda.buscar_contacto(43423211))
print(agenda.buscar_contacto(12345678))
print(agenda.buscar_contacto(99999999))