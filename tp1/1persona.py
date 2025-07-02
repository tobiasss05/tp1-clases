class Persona:
    def __init__(self, nombre, edad, altura):
        """Inicializa las propiedades de la persona."""
        self.nombre = nombre  # Establece el nombre
        self.edad = edad      # Establece la edad
        self.altura = altura  # Establece la altura

    def obtener_nombre(self):
        """Devuelve el nombre de la persona."""
        return self.nombre

    def establecer_nombre(self, nombre):
        """Establece un nuevo nombre para la persona."""
        self.nombre = nombre

    def obtener_edad(self):
        """Devuelve la edad de la persona."""
        return self.edad

    def establecer_edad(self, edad):
        """Establece una nueva edad para la persona."""
        self.edad = edad

    def obtener_altura(self):
        """Devuelve la altura de la persona."""
        return self.altura

    def establecer_altura(self, altura):
        """Establece una nueva altura para la persona."""
        self.altura = altura

# Ejemplo de uso de la clase Persona
if __name__ == "__main__":
    # Crear una instancia de Persona
    persona1 = Persona("Juan", 30, 1.75)

    # Obtener y mostrar las propiedades
    print(f"Nombre: {persona1.obtener_nombre()}")
    print(f"Edad: {persona1.obtener_edad()}")
    print(f"Altura: {persona1.obtener_altura()} m")

    # Establecer nuevas propiedades
    persona1.establecer_nombre("Tobias")
    persona1.establecer_edad(19)
    persona1.establecer_altura(1.80)

    # Mostrar las propiedades actualizadas
    print("\nDespués de actualizar:")
    print(f"Nombre: {persona1.obtener_nombre()}")
    print(f"Edad: {persona1.obtener_edad()}")
    print(f"Altura: {persona1.obtener_altura()} m")
