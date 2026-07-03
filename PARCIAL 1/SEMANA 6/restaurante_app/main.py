from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante

if __name__ == "__main__":
    #Crear clase de servicio
    mi_restaurante = Restaurante()

    #Crear al menos dos objetos de tipo Platillo y dos de tipo Bebida
    plato1 = Platillo("Encebollado", 4.50, 650)
    plato2 = Platillo("Seco de Pollo", 3.50, 800)

    bebida1 = Bebida("Jugo de Naranjilla", 1.50, 400)
    bebida2 = Bebida("Agua Mineral", 1.00, 500)

    #Agregar objetos a la lista administrada por Restaurante
    mi_restaurante.agregar_producto(plato1)
    mi_restaurante.agregar_producto(plato2)
    mi_restaurante.agregar_producto(bebida1)
    mi_restaurante.agregar_producto(bebida2)

    #Mostrar la información de forma organizada en consola
    mi_restaurante.mostrar_informacion()

    #Prueba de validación de precio (No debe cambiar a negativo)
    print("\n--- Prueba de Validación de Precio ---")
    bebida2.cambiar_precio(-0.50)