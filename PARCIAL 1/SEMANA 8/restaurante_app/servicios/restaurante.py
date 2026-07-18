from typing import List
from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    def __init__(self) -> None:
        self._productos: List[Producto] = []
        self._clientes: List[Cliente] = []

    def registrar_producto(self, nuevo_producto: Producto) -> bool:
        if self._existe_codigo_producto(nuevo_producto.codigo):
            return False
        self._productos.append(nuevo_producto)
        return True

    def registrar_cliente(self, nuevo_cliente: Cliente) -> bool:
        if self._existe_identificacion_cliente(nuevo_cliente.identificacion):
            return False
        self._clientes.append(nuevo_cliente)
        return True

    def obtener_productos(self) -> List[Producto]:
        return self._productos

    def obtener_clientes(self) -> List[Cliente]:
        return self._clientes

    def _existe_codigo_producto(self, codigo: str) -> bool:
        for producto_existente in self._productos:
            if producto_existente.codigo == codigo:
                return True
        return False

    def _existe_identificacion_cliente(self, identificacion: str) -> bool:
        for cliente_existente in self._clientes:
            if cliente_existente.identificacion == identificacion:
                return True
        return False