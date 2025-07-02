class Empleado:
    def __init__(self, nombre, edad, salario, cargo):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
        self.cargo = cargo

    def obtener_nombre(self):
        return self.nombre

    def establecer_nombre(self, nombre):
        self.nombre = nombre

    def obtener_edad(self):
        return self.edad

    def establecer_edad(self, edad):
        self.edad = edad

    def obtener_salario(self):
        return self.salario

    def establecer_salario(self, salario):
        self.salario = salario

    def obtener_cargo(self):
        return self.cargo

    def establecer_cargo(self, cargo):
        self.cargo = cargo

    def calcular_salario_anual(self):
        return self.salario * 12

if __name__ == "__main__":
    empleado1 = Empleado("Pedro López", 45, 3000, "Gerente")
    print(f"Nombre: {empleado1.obtener_nombre()}")
    print(f"Edad: {empleado1.obtener_edad()}")
    print(f"Salario mensual: ${empleado1.obtener_salario():.2f}")
    print(f"Cargo: {empleado1.obtener_cargo()}")
    print(f"Salario anual: ${empleado1.calcular_salario_anual():.2f}")

    empleado1.establecer_salario(3200)
    print(f"\nDespués de aumentar el salario:")
    print(f"Nuevo salario mensual: ${empleado1.obtener_salario():.2f}")
    print(f"Nuevo salario anual: ${empleado1.calcular_salario_anual():.2f}")