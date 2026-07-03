from modelos.producto import Producto

class Platillo(Producto):
    def __init__(self, nombre, precio, calorias, disponibilidad=True):
        #Uso de super() para heredar atributos comunes
        super().__init__(nombre, precio, disponibilidad)
        self.calorias = calorias  # Atributo propio

    #Sobrescribir metodo para demostrar polimorfismo
    def mostrar_informacion(self):
        info_padre = super().mostrar_informacion()
        return f"{info_padre} | Calorías: {self.calorias} kcal"