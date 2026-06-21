#Importa las clases de los otros archivos
from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def main():
    #Crea el restaurante principal
    mi_restaurante = Restaurante("Sabor Ecuatoriano")

    #Crea los productos
    prod1 = Producto("Encebollado", 2.50)
    prod2 = Producto("Ceviche de camaron", 3.50)

    #Crea los clientes
    clie1 = Cliente("Carlos Mendoza", "0987654321")
    clie2 = Cliente("Ana Palacios", "1234567890")

    #Guarda los productos y clientes en el restaurante
    mi_restaurante.registrar_producto(prod1)
    mi_restaurante.registrar_producto(prod2)
    mi_restaurante.registrar_cliente(clie1)
    mi_restaurante.registrar_cliente(clie2)

    #Imprime la informacion final
    mi_restaurante.mostrar_informacion()


if __name__ == "__main__":
    main()