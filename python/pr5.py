print("Sepulveda Gonzalez Angel Alejandro,3W,1215")
print("")
class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
    def mostrar(self):
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}, Email: {self.email}"
#definir clase llamada agenda
class Agenda:
    def __init__(self):
        self.contactos = []
    def añadir_contacto(self):
        nombre = input("Introduce el nombre del contacto: ")
        telefono = input("Introduce el teléfono del contacto: ")
        email = input("Introduce el email del contacto: ")
        nuevo_contacto = Contacto(nombre, telefono, email)
        self.contactos.append(nuevo_contacto)
        print("Contacto añadido exitosamente.")
    def lista_contactos(self):
        if not self.contactos:
            print("No hay contactos en la agenda.")
        else:
            for contacto in self.contactos:
                print(contacto.mostrar())

    def buscar_contacto(self):
        nombre_buscar = input("Introduce el nombre del contacto a buscar: ")
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre_buscar.lower():
                print(contacto.mostrar())
                return
        print("Contacto no encontrado.")
    def editar_contacto(self):
        nombre_buscar = input("Introduce el nombre del contacto a editar: ")
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre_buscar.lower():
                nuevo_telefono = input(f"Introduce el nuevo teléfono de {contacto.nombre}: ")
                nuevo_email = input(f"Introduce el nuevo email de {contacto.nombre}: ")
                contacto.telefono = nuevo_telefono
                contacto.email = nuevo_email
                print("Contacto editado exitosamente.")
                return
        print("Contacto no encontrado.")
    def cerrar_agenda(self):
        print("Cerrando la agenda... Hasta luego.")
        exit()
    def mostrar_menu(self):
        while True:
            print("\n---- MENÚ DE AGENDA ----")
            print("1. Añadir contacto")
            print("2. Lista de contactos")
            print("3. Buscar contacto")
            print("4. Editar contacto")
            print("5. Cerrar agenda")
            opcion = input("Selecciona una opción (1-5): ")
            if opcion == "1":
                self.añadir_contacto()
            elif opcion == "2":
                self.lista_contactos()
            elif opcion == "3":
                self.buscar_contacto()
            elif opcion == "4":
                self.editar_contacto()
            elif opcion == "5":
                self.cerrar_agenda()
            else:
                print("Opción no válida.")
# Ejemplo de uso
agenda = Agenda()
agenda.mostrar_menu()