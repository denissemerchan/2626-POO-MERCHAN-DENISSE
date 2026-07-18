from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente

def mostrar_menu() -> None:
    print("\n=======================================")
    print("        SISTEMA DE RESTAURANTE        ")
    print("=======================================")
    print("1. Registrar producto")
    print("2. Registrar bebida")
    print("3. Registrar cliente")
    print("---------------------------------------")
    print("4. Listar productos")
    print("5. Listar clientes")
    print("---------------------------------------")
    print("6. Salir")

def ejecutar_sistema() -> None:
    servicio_restaurante: Restaurante = Restaurante()

    while True:
        mostrar_menu()
        opcion: str = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            print("\n--- Registrar Producto ---")
            codigo: str = input("Código: ").strip()
            nombre: str = input("Nombre: ").strip()
            categoria: str = input("Categoría: ").strip()
            try:
                precio: float = float(input("Precio: "))
                un_producto: Producto = Producto(codigo, nombre, categoria, precio)
                if servicio_restaurante.registrar_producto(un_producto):
                    print("¡Producto registrado con éxito!")
                else:
                    print("Error: El código de producto ya se encuentra registrado.")
            except ValueError:
                print("Error: El precio ingresado debe ser un número válido.")

        elif opcion == "2":
            print("\n--- Registrar Bebida ---")
            codigo: str = input("Código: ").strip()
            nombre: str = input("Nombre: ").strip()
            categoria: str = input("Categoría: ").strip()
            try:
                precio: float = float(input("Precio: "))
                tamano: str = input("Tamaño (ej. 500ml): ").strip()
                tipo_envase: str = input("Tipo de envase (ej. Plástico): ").strip()
                una_bebida: Bebida = Bebida(codigo, nombre, categoria, precio, tamano, tipo_envase)
                if servicio_restaurante.registrar_producto(una_bebida):
                    print("¡Bebida registrada con éxito!")
                else:
                    print("Error: El código de producto/bebida ya se encuentra registrado.")
            except ValueError:
                print("Error: El precio ingresado debe ser un número válido.")

        elif opcion == "3":
            print("\n--- Registrar Cliente ---")
            identificacion: str = input("Identificación: ").strip()
            nombre: str = input("Nombre: ").strip()
            correo: str = input("Correo electrónico: ").strip()
            un_cliente: Cliente = Cliente(identificacion, nombre, correo)
            if servicio_restaurante.registrar_cliente(un_cliente):
                print("¡Cliente registrado con éxito!")
            else:
                print("Error: La identificación del cliente ya se encuentra registrada.")

        elif opcion == "4":
            print("\n--- Listado de Productos ---")
            lista_productos = servicio_restaurante.obtener_productos()
            if not lista_productos:
                print("No hay productos ni bebidas en el sistema.")
            else:
                for item_producto in lista_productos:
                    item_producto.mostrar_informacion()

        elif opcion == "5":
            print("\n--- Listado de Clientes ---")
            lista_clientes = servicio_restaurante.obtener_clientes()
            if not lista_clientes:
                print("No hay clientes registrados en el sistema.")
            else:
                for item_cliente in lista_clientes:
                    item_cliente.mostrar_informacion()

        elif opcion == "6":
            print("\nSaliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    ejecutar_sistema()