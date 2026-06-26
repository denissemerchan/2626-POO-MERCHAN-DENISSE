from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.cliente import Cliente


def ejecutar_sistema() -> None:
    #Crear el servicio principal
    mi_restaurante = Restaurante("Sabor del Ecuador")

    print("--- REGISTRANDO DATOS ---")
    #Crear e incluir al menos dos objetos de tipo Producto
    producto_uno = Producto("Encebollado Mixto", 2.50, True)
    producto_dos = Producto("Jugo de Naranja Natural", 0.75, False)

    mi_restaurante.agregar_producto(producto_uno)
    mi_restaurante.agregar_producto(producto_dos)

    #Crear e incluir al menos dos objetos de tipo Cliente
    cliente_uno = Cliente("Carlos Alvarado", 4, True)
    cliente_dos = Cliente("María José Romero", 2, False)

    mi_restaurante.registrar_cliente(cliente_uno)
    mi_restaurante.registrar_cliente(cliente_dos)

    #Mostrar la información registrada de forma organizada en la consola
    mi_restaurante.mostrar_menu_y_clientes()


if __name__ == "__main__":
    ejecutar_sistema()