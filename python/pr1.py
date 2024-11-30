print("Sepulveda Gonzalez Angel Alejandro,3W,1215")
print("")
# clase llamada Alumno
class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre #definir atributo nombre
        self.nota = nota #definir atributo nota
#definir atributos de texto
    def imprimir_datos(self):
        print(f"Alumno: {self.nombre}")
        print(f"Nota: {self.nota}")
#mostrar mensaje
    def resultado(self):
        if self.nota >= 6:
            print(f"{self.nombre} ha aprobado.")
        else:
            print(f"{self.nombre} ha suspendido.")
# Entrada de datos
nombre = input("Introduce el nombre del alumno: ")
nota = float(input("Introduce la nota del alumno: "))
alumno1 = Alumno(nombre, nota)
alumno1.imprimir_datos()
alumno1.resultado()

