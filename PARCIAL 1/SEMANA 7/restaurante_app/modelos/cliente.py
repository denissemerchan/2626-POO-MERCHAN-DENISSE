from dataclasses import dataclass

#Modelado simplificado de la entidad Cliente usando dataclass
@dataclass
class Cliente:
    nombre: str
    correo: str
    id_cliente: str

    def mostrar_informacion(self):
        print(f"ID: {self.id_cliente} | Cliente: {self.nombre} | Correo: {self.correo}")