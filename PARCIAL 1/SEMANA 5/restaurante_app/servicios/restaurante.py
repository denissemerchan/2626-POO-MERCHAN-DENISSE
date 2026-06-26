from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    def __init__(self, nombre_establecimiento: str):
        self.nombre_establecimiento: str = nombre_establecimiento
        self.lista_productos: list[Producto] = []
        self.lista_clientes: list[Cliente] = []

    def agregar_producto(self, nuevo_producto: Producto) -> None:
        self.lista_productos.append(nuevo_producto)
        print(f"✓ Producto '{nuevo_producto.nombre}' registrado correctamente.")

    def registrar_cliente(self, nuevo_cliente: Cliente) -> None:
        self.lista_clientes.append(nuevo_cliente)
        print(f"✓ Cliente '{nuevo_cliente.nombre_completo}' registrado con éxito.")

    def mostrar_menu_y_clientes(self) -> None:
        print(f"\n--- INFORMACIÓN DE: {self.nombre_establecimiento.upper()} ---")

        print("\nMenú del Día:")
        for producto in self.lista_productos:
            print(f"  - {producto}")

        print("\nClientes en el Establecimiento:")
        for cliente in self.lista_clientes:
            print(f"  - {cliente}")