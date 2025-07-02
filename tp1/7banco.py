class Banco:
    def __init__(self, nombre_banco, tasa_interes):
        self.nombre_banco = nombre_banco
        self.tasa_interes = tasa_interes

    def obtener_nombre_banco(self):
        return self.nombre_banco

    def establecer_nombre_banco(self, nombre_banco):
        self.nombre_banco = nombre_banco

    def obtener_tasa_interes(self):
        return self.tasa_interes

    def establecer_tasa_interes(self, tasa_interes):
        self.tasa_interes = tasa_interes

    def calcular_interes(self, capital, tiempo_años):
        return capital * self.tasa_interes * tiempo_años

    def tiempo_duplicar_cantidad(self):
        if self.tasa_interes > 0:
            return 72 / (self.tasa_interes * 100)
        return float('inf')

if __name__ == "__main__":
    banco1 = Banco("MiBanco", 0.05)
    print(f"Nombre del banco: {banco1.obtener_nombre_banco()}")
    print(f"Tasa de interés: {banco1.obtener_tasa_interes() * 100}%")

    capital_inicial = 1000
    años = 5
    interes_obtenido = banco1.calcular_interes(capital_inicial, años)
    print(f"Interés obtenido en ${capital_inicial} en {años} años: ${interes_obtenido:.2f}")

    tiempo_duplicar = banco1.tiempo_duplicar_cantidad()
    print(f"Tiempo para duplicar la cantidad (Regla del 72): {tiempo_duplicar:.2f} años")

    banco1.establecer_tasa_interes(0.06)
    print(f"\nNueva tasa de interés: {banco1.obtener_tasa_interes() * 100}%")
    print(f"Nuevo tiempo para duplicar: {banco1.tiempo_duplicar_cantidad():.2f} años")