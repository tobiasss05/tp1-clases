class Libro:
    def __init__(self, titulo, autor, genero, numero_paginas):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.numero_paginas = numero_paginas

    def obtener_titulo(self):
        return self.titulo

    def establecer_titulo(self, titulo):
        self.titulo = titulo

    def obtener_autor(self):
        return self.autor

    def establecer_autor(self, autor):
        self.autor = autor

    def obtener_genero(self):
        return self.genero

    def establecer_genero(self, genero):
        self.genero = genero

    def obtener_numero_paginas(self):
        return self.numero_paginas

    def establecer_numero_paginas(self, numero_paginas):
        self.numero_paginas = numero_paginas

    def es_ficcion(self):
        generos_ficcion = ["ficción", "ciencia ficción", "fantasía", "novela", "thriller", "misterio", "terror"]
        return self.genero.lower() in generos_ficcion

if __name__ == "__main__":
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 496)
    print(f"Título: {libro1.obtener_titulo()}")
    print(f"Autor: {libro1.obtener_autor()}")
    print(f"Género: {libro1.obtener_genero()}")
    print(f"Número de páginas: {libro1.obtener_numero_paginas()}")
    print(f"¿Es de ficción? {libro1.es_ficcion()}")

    libro2 = Libro("Sapiens: De animales a dioses", "Yuval Noah Harari", "Historia", 512)
    print(f"\nTítulo: {libro2.obtener_titulo()}")
    print(f"Género: {libro2.obtener_genero()}")
    print(f"¿Es de ficción? {libro2.es_ficcion()}")

    libro1.establecer_genero("Ciencia Ficción")
    print(f"\nDespués de actualizar el género de '{libro1.obtener_titulo()}': {libro1.obtener_genero()}")
    print(f"¿Es de ficción ahora? {libro1.es_ficcion()}")