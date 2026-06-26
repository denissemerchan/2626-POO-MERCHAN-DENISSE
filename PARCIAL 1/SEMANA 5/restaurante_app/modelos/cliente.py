class Cliente:
    def __init__(self, nombre_completo: str, mesa_asignada: int, es_frecuente: bool):
        self.nombre_completo: str = nombre_completo
        self.mesa_asignada: int = mesa_asignada
        self.es_frecuente: bool = es_frecuente

    def __str__(self) -> str:
        tipo_cliente = "Frecuente" if self.es_frecuente else "Regular"
        return f"Cliente: {self.nombre_completo} | Mesa: {self.mesa_asignada} | Tipo: {tipo_cliente}"