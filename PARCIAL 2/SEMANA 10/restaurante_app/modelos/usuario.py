class Usuario:
    def __init__(self, id_usuario: int, nombre: str, rol: str) -> None:
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.rol = rol

    def __str__(self) -> str:
        return f"Usuario ID: {self.id_usuario} | Nombre: {self.nombre} | Rol: {self.rol}"