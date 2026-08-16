from typing import List, Set, Dict, Optional
from modelos.producto import Producto
from modelos.usuario import Usuario

class Restaurante:
    def __init__(self) -> None:
        self.lista_productos: List[Producto] = []
        self.lista_usuarios: List[Usuario] = []

    def registrar_producto(self, producto: Producto) -> bool:
        for p in self.lista_productos:
            if p.codigo == producto.codigo:
                return False
        self.lista_productos.append(producto)
        return True

    def buscar_producto(self, codigo: str) -> Optional[Producto]:
        for p in self.lista_productos:
            if p.codigo == codigo:
                return p
        return None

    def actualizar_producto(self, codigo: str, nuevo_nombre: str, nueva_categoria: str, nuevo_precio: float) -> bool:
        producto = self.buscar_producto(codigo)
        if producto:
            producto.nombre = nuevo_nombre
            producto.categoria = nueva_categoria
            producto.precio = nuevo_precio
            return True
        return False

    def eliminar_producto(self, codigo: str) -> bool:
        producto = self.buscar_producto(codigo)
        if producto:
            self.lista_productos.remove(producto)
            return True
        return False

    def registrar_usuario(self, usuario: Usuario) -> bool:
        for u in self.lista_usuarios:
            if u.identificacion == usuario.identificacion:
                return False
        self.lista_usuarios.append(usuario)
        return True

    def obtener_categorias(self) -> Set[str]:
        categorias: Set[str] = set()
        for p in self.lista_productos:
            categorias.add(p.categoria)
        return categorias

    def obtener_menu_opciones(self) -> Dict[str, str]:
        return {
            "1": "Registrar producto",
            "2": "Buscar producto",
            "3": "Actualizar producto",
            "4": "Eliminar producto",
            "5": "Listar productos",
            "6": "Registrar usuario",
            "7": "Listar usuarios",
            "8": "Mostrar categorías",
            "9": "Salir"
        }