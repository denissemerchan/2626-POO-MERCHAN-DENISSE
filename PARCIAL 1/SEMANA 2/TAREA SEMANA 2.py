class Mascota:
    def __init__(self, nombre, especie, edad, duenio):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.duenio = duenio

    def descripcion(self):
        return f"{self.nombre} es un(a) {self.especie} de {self.edad} año(s) y su dueño(a) es {self.duenio}."

    def cumplir_anios(self):
        self.edad += 1
        return f"¡Feliz cumpleaños, {self.nombre}! Ahora tiene {self.edad} año(s)."


if __name__ == '__main__':
    mascota1 = Mascota(nombre='Luna', especie='gato', edad=3, duenio='Denisse')
    mascota2 = Mascota(nombre='Max', especie='perro', edad=5, duenio='Alicia')

    print(mascota1.descripcion())
    print(mascota2.descripcion())
    print(mascota1.cumplir_anios())
    print(mascota2.cumplir_anios())
