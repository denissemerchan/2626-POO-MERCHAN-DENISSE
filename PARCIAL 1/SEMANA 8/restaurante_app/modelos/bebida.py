from modelos.producto import Producto

class Bebida(Producto):
    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float, tamano: str, tipo_envase: str) -> None:
        super().__init__(codigo, nombre, categoria, precio)
        self.tamano: str = tamano
        self.tipo_envase: str = tipo_envase

    def mostrar_informacion(self) -> None:
        print(f"[{self.categoria}] Código: {self.codigo} | Nombre: {self.nombre} | Precio: ${self.precio:.2f} | Tamaño: {self.tamano} | Envase: {self.tipo_envase}")