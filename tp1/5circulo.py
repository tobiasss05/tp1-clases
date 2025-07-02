class Circulo:
    def __init__(self, radio):
        self.radio = radio
        self.diametro = 2 * radio

    def obtener_radio(self):
        return self.radio

    def establecer_radio(self, radio):
        self.radio = radio
        self.diametro = 2 * radio

    def obtener_diametro(self):
        return self.diametro

    def establecer_diametro(self, diametro):
        self.diametro = diametro
        self.radio = diametro / 2

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

    def calcular_circunferencia(self):
        return 2 * math.pi * self.radio

if __name__ == "__main__":
    circulo1 = Circulo(5)
    print(f"Radio: {circulo1.obtener_radio()}")
    print(f"Diámetro: {circulo1.obtener_diametro()}")
    print(f"Área: {circulo1.calcular_area():.2f}")
    print(f"Circunferencia: {circulo1.calcular_circunferencia():.2f}")

    circulo1.establecer_diametro(12)
    print(f"\nDespués de actualizar el diámetro:")
    print(f"Radio: {circulo1.obtener_radio()}")
    print(f"Área: {circulo1.calcular_area():.2f}")
    print(f"Circunferencia: {circulo1.calcular_circunferencia():.2f}")