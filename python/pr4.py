print("Sepulveda Gonzalez Angel Alejandro,3W,1215")
print("")
class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def suma(self):
        return self.num1 + self.num2
    def resta(self):
        return self.num1 - self.num2
    def multiplicacion(self):
        return self.num1 * self.num2
    def division(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Error: No se puede dividir por cero."
# Entrada de datos
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
calc = Calculadora(num1, num2)
print(f"Suma: {calc.suma()}")
print(f"Resta: {calc.resta()}")
print(f"Multiplicación: {calc.multiplicacion()}")
print(f"División: {calc.division()}")
