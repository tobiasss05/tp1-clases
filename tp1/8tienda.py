class Tienda:
    def __init__(self, nombre_tienda):
        self.nombre_tienda = nombre_tienda
        self.productos_disponibles = []

    def obtener_nombre_tienda(self):
        return self.nombre_tienda

    def establecer_nombre_tienda(self, nombre_tienda):
        self.nombre_tienda = nombre_tienda

    def añadir_producto(self, producto):
        if producto not in self.productos_disponibles:
            self.productos_disponibles.append(producto)
            print(f"'{producto}' ha sido añadido a la tienda.")
        else:
            print(f"'{producto}' ya está en la tienda.")

    def eliminar_producto(self, producto):
        if producto in self.productos_disponibles:
            self.productos_disponibles.remove(producto)
            print(f"'{producto}' ha sido eliminado de la tienda.")
        else:
            print(f"'{producto}' no se encuentra en la tienda.")

    def obtener_lista_productos(self):
        return self.productos_disponibles

if __name__ == "__main__":
    tienda1 = Tienda("Mi Tienda Online")
    print(f"Nombre de la tienda: {tienda1.obtener_nombre_tienda()}")

    tienda1.añadir_producto("Laptop")
    tienda1.añadir_producto("Teclado")
    tienda1.añadir_producto("Ratón")
    print(f"Productos en stock: {tienda1.obtener_lista_productos()}")

    tienda1.eliminar_producto("Teclado")
    print(f"Productos después de eliminar: {tienda1.obtener_lista_productos()}")

    tienda1.añadir_producto("Laptop")
    tienda1.eliminar_producto("Monitor")