class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.notas = []

    def obtener_nombre(self):
        return self.nombre

    def establecer_nombre(self, nombre):
        self.nombre = nombre

    def obtener_edad(self):
        return self.edad

    def establecer_edad(self, edad):
        self.edad = edad

    def obtener_carrera(self):
        return self.carrera

    def establecer_carrera(self, carrera):
        self.carrera = carrera

    def añadir_nota(self, nota):
        if 0 <= nota <= 100:
            self.notas.append(nota)
        else:
            print("La nota debe estar entre 0 y 100.")

    def calcular_nota_media(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)

if __name__ == "__main__":
    estudiante1 = Estudiante("Ana García", 20, "Ingeniería Informática")
    print(f"Nombre: {estudiante1.obtener_nombre()}")
    print(f"Edad: {estudiante1.obtener_edad()}")
    print(f"Carrera: {estudiante1.obtener_carrera()}")

    estudiante1.añadir_nota(85)
    estudiante1.añadir_nota(92)
    estudiante1.añadir_nota(78)
    print(f"Notas: {estudiante1.notas}")
    print(f"Nota media: {estudiante1.calcular_nota_media():.2f}")

    estudiante1.establecer_edad(21)
    print(f"\nDespués de actualizar la edad: {estudiante1.obtener_edad()}")