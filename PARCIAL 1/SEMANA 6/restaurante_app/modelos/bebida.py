from modelos.producto import Producto

class Bebida(Producto):
    def __init__(self, nombre, precio, volumen_ml, disponibilidad=True):
        #Uso de super() para heredar atributos comunes
        super().__init__(nombre, precio, disponibilidad)
        self.volumen_ml = volumen_ml  #Atributo propio

    #Sobrescribir metodo para demostrar polimorfismo
    def mostrar_informacion(self):
        info_padre = super().mostrar_informacion()
        return f"{info_padre} | Volumen: {self.volumen_ml} ml"