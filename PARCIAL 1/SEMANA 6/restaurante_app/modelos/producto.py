class Producto:
    def __init__(self, nombre, precio, disponibilidad=True):
        self.nombre = nombre
        #Atributo privado encapsulado
        self.__precio = 0.0
        self.cambiar_precio(precio)
        self.disponibilidad = disponibilidad

    #Métodos de acceso y modificación
    def obtener_precio(self):
        return self.__precio

    def cambiar_precio(self, nuevo_precio):
        #Validación para que no sea negativo ni cero
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print(f"Error: El precio de '{self.nombre}' debe ser mayor a cero.")

    def mostrar_informacion(self):
        estado = "Disponible" if self.disponibilidad else "Agotado"
        return f"Producto: {self.nombre} | Precio: ${self.__precio:.2f} | Estado: {estado}"