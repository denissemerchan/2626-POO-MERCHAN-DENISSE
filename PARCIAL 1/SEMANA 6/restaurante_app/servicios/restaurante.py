class Restaurante:
    def __init__(self):
        #Lista para almacenar los productos registrados
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_informacion(self):
        print("\n=== MENÚ DEL RESTAURANTE ===")
        #Polimorfismo en acción al recorrer la lista y ejecutar mostrar_informacion()
        for producto in self.productos:
            print(producto.mostrar_informacion())