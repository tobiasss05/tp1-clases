class Rectangulo:
    def __init__(self, longitud, anchura):
        self.longitud = longitud
        self.anchura = anchura

    def obtener_longitud(self):
        return self.longitud

    def establecer_longitud(self, longitud):
        self.longitud = longitud

    def obtener_anchura(self):
        return self.anchura

    def establecer_anchura(self, anchura):
        self.anchura = anchura

    def calcular_area(self):
        return self.longitud * self.anchura

    def calcular_perimetro(self):
        return 2 * (self.longitud + self.anchura)

if __name__ == "__main__":
    rectangulo1 = Rectangulo(10, 5)
    print(f"Longitud: {rectangulo1.obtener_longitud()}")
    print(f"Anchura: {rectangulo1.obtener_anchura()}")
    print(f"Área: {rectangulo1.calcular_area()}")
    print(f"Perímetro: {rectangulo1.calcular_perimetro()}")

    rectangulo1.establecer_longitud(12)
    print(f"\nDespués de actualizar la longitud:")
    print(f"Área: {rectangulo1.calcular_area()}")
    print(f"Perímetro: {rectangulo1.calcular_perimetro()}")