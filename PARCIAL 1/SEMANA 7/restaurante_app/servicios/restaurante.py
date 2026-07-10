from modelos.producto import Producto
from modelos.cliente import Cliente

#Servicio encargado de gestionar las colecciones del sistema
class Restaurante:
    def __init__(self):
        self.lista_productos = []
        self.lista_clientes = []

    #Métodos para la gestión de Productos
    def registrar_producto(self, producto: Producto):
        self.lista_productos.append(producto)
        print("¡Producto registrado con éxito!")

    def listar_productos(self):
        if not self.lista_productos:
            print("No hay productos registrados en el sistema.")
            return
        for prod in self.lista_productos:
            prod.mostrar_informacion()

    def buscar_producto(self, nombre_buscar: str):
        encontrados = [p for p in self.lista_productos if nombre_buscar.lower() in p.nombre.lower()]
        if not encontrados:
            print(f"No se encontró ningún producto que coincida con '{nombre_buscar}'.")
            return
        for prod in encontrados:
            prod.mostrar_informacion()

    #Métodos para la gestión de Clientes
    def registrar_cliente(self, cliente: Cliente):
        self.lista_clientes.append(cliente)
        print("¡Cliente registrado con éxito!")

    def listar_clientes(self):
        if not self.lista_clientes:
            print("No hay clientes registrados en el sistema.")
            return
        for cli in self.lista_clientes:
            cli.mostrar_informacion()

    def buscar_cliente(self, id_buscar: str):
        encontrados = [c for c in self.lista_clientes if id_buscar.strip() == c.id_cliente.strip()]
        if not encontrados:
            print(f"No se encontró ningún cliente con el ID '{id_buscar}'.")
            return
        for cli in encontrados:
            cli.mostrar_informacion()