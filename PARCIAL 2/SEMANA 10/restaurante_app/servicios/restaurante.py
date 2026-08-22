from typing import List, Optional
from modelos.producto import Producto
from modelos.usuario import Usuario

class Restaurante:
    def __init__(self) -> None:
        self._productos: List[Producto] = []
        self._usuarios: List[Usuario] = []

    def obtener_productos(self) -> List[Producto]:
        return self._productos

    def establecer_productos(self, productos: List[Producto]) -> None:
        self._productos = productos

    def registrar_producto(self, producto: Producto) -> bool:
        if self.buscar_producto_por_id(producto.id_producto) is not None:
            print("[Error] Ya existe un producto registrado con ese ID.")
            return False
        self._productos.append(producto)
        return True

    def buscar_producto_por_id(self, id_producto: int) -> Optional[Producto]:
        for prod in self._productos:
            if prod.id_producto == id_producto:
                return prod
        return None

    def actualizar_producto(self, id_producto: int, nuevo_nombre: str, nuevo_precio: float) -> bool:
        prod = self.buscar_producto_por_id(id_producto)
        if prod:
            prod.nombre = nuevo_nombre
            prod.precio = nuevo_precio
            return True
        return False

    def eliminar_producto(self, id_producto: int) -> bool:
        prod = self.buscar_producto_por_id(id_producto)
        if prod:
            self._productos.remove(prod)
            return True
        return False

    def registrar_usuario(self, usuario: Usuario) -> None:
        self._usuarios.append(usuario)

    def listar_usuarios(self) -> List[Usuario]:
        return self._usuarios