class Producto:
    def __init__(self, nombre, precio, stock_disponible):
        self.nombre = nombre
        self.precio = precio
        self.stock_disponible = stock_disponible

    def obtener_nombre(self):
        return self.nombre

    def establecer_nombre(self, nombre):
        self.nombre = nombre

    def obtener_precio(self):
        return self.precio

    def establecer_precio(self, precio):
        self.precio = precio

    def obtener_stock_disponible(self):
        return self.stock_disponible

    def aumentar_stock(self, cantidad):
        if cantidad > 0:
            self.stock_disponible += cantidad
        else:
            print("La cantidad a aumentar debe ser positiva.")

    def disminuir_stock(self, cantidad):
        if cantidad > 0:
            if self.stock_disponible >= cantidad:
                self.stock_disponible -= cantidad
            else:
                print("No hay suficiente stock disponible.")
        else:
            print("La cantidad a disminuir debe ser positiva.")

if __name__ == "__main__":
    producto1 = Producto("remera", 25.000, 100)
    print(f"Producto: {producto1.obtener_nombre()}")
    print(f"Precio: ${producto1.obtener_precio():.2f}")
    print(f"Stock: {producto1.obtener_stock_disponible()}")

    producto1.aumentar_stock(50)
    print(f"Stock después de aumentar: {producto1.obtener_stock_disponible()}")

    producto1.disminuir_stock(30)
    print(f"Stock después de disminuir: {producto1.obtener_stock_disponible()}")

    producto1.disminuir_stock(150)  