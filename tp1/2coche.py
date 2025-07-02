class Coche:
    def __init__(self, marca, modelo, año_fabricacion):
        self.marca = marca
        self.modelo = modelo
        self.año_fabricacion = año_fabricacion

    def obtener_marca(self):
        return self.marca

    def establecer_marca(self, marca):
        self.marca = marca

    def obtener_modelo(self):
        return self.modelo

    def establecer_modelo(self, modelo):
        self.modelo = modelo

    def obtener_año_fabricacion(self):
        return self.año_fabricacion

    def establecer_año_fabricacion(self, año_fabricacion):
        self.año_fabricacion = año_fabricacion

    def años_desde_fabricacion(self):
        from datetime import datetime
        año_actual = datetime.now().year
        return año_actual - self.año_fabricacion

if __name__ == "__main__":
    coche1 = Coche("Toyota", "Corolla", 2015)
    print(f"Marca: {coche1.obtener_marca()}")
    print(f"Modelo: {coche1.obtener_modelo()}")
    print(f"Año de fabricación: {coche1.obtener_año_fabricacion()}")
    print(f"Años desde fabricación: {coche1.años_desde_fabricacion()}")

    coche1.establecer_modelo("Corolla")
    print(f"\nDespués de actualizar el modelo: {coche1.obtener_modelo()}")