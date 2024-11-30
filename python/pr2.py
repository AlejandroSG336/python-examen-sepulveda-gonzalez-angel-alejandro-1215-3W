print("Sepulveda Gonzalez Angel Alejandro,3W,1215")
print("")
#clase llamada persona
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre #definir atributo nombre
        self.edad = edad #definir atributo edad
#definir atributos de texto
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
#mostrar mensaje
    def es_mayor_de_edad(self):
        if self.edad >= 18:
            print(f"{self.nombre} es mayor de edad.")
        else:
            print(f"{self.nombre} no es mayor de edad.")
# Entrada de datos
nombre = input("Introduce el nombre de la persona: ")
edad = int(input("Introduce la edad de la persona: "))
persona1 = Persona(nombre, edad)
persona1.mostrar_datos()
persona1.es_mayor_de_edad()
