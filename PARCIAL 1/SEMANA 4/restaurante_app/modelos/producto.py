class Producto:
    def __init__(self, nombre, precio):
        #Guarda informacion sobre nombre y precio
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        #Devuelve el producto como texto
        return f"Producto: {self.nombre} - ${self.precio:.2f}"