class Producto:
    def __init__(self, id_producto: int, nombre: str, precio: float) -> None:
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio

    @property
    def id_producto(self) -> int:
        return self._id_producto

    @id_producto.setter
    def id_producto(self, valor: int) -> None:
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("El ID debe ser un número entero positivo.")
        self._id_producto = valor

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = valor.strip()

    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, valor: float) -> None:
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("El precio debe ser un número mayor a cero.")
        self._precio = float(valor)

    def a_diccionario(self) -> dict:
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "precio": self.precio
        }

    def __str__(self) -> str:
        return f"ID: {self.id_producto} | Nombre: {self.nombre} | Precio: ${self.precio:.2f}"