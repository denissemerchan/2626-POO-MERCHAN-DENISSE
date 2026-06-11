class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Especie: {self.especie}, Edad: {self.edad}")

    def hacer_sonido(self):
        print(f"{self.nombre} hace un sonido.")