class Cliente:
    def __init__(self, nombre, cedula):
        #Guarda el nombre y la cédula
        self.nombre = nombre
        self.cedula = cedula

    def __str__(self):
        #Devuelve el cliente como texto
        return f"Cliente: {self.nombre} (C.I.: {self.cedula})"