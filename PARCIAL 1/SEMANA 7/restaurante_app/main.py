import sys
import os

#Ajuste del path de ejecución para importaciones modulares nativas
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.cliente import Cliente


def mostrar_menu():
    print("\n======================================================")
    print("        SISTEMA DE RESTAURANTE: SABOR ECUATORIANO       ")
    print("======================================================")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("--------------------------------------------------------")
    print("4. Registrar cliente")
    print("5. Listar clientes")
    print("6. Buscar cliente")
    print("--------------------------------------------------------")
    print("7. Salir")


def ejecutar_sistema():
    servicio = Restaurante()

    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ").strip()

        try:
            if opcion == "1":
                print("\n--- Registro de Producto ---")
                nombre = input("Nombre del producto: ")
                categoria = input("Categoría: ")
                precio = float(input("Precio: "))
                nuevo_prod = Producto(nombre, categoria, precio)
                servicio.registrar_producto(nuevo_prod)

            elif opcion == "2":
                print("\n--- Lista de Productos ---")
                servicio.listar_productos()

            elif opcion == "3":
                print("\n--- Buscar Producto ---")
                nombre_buscar = input("Ingrese el nombre a buscar: ")
                servicio.buscar_producto(nombre_buscar)

            elif opcion == "4":
                print("\n--- Registro de Cliente ---")
                nombre = input("Nombre completo del cliente: ")
                correo = input("Correo electrónico: ")
                id_cliente = input("Identificador único (ID): ")

                if not nombre.strip() or not correo.strip() or not id_cliente.strip():
                    print("Error: Ningún campo del cliente puede estar vacío.")
                    continue

                nuevo_cli = Cliente(nombre, correo, id_cliente)
                servicio.registrar_cliente(nuevo_cli)

            elif opcion == "5":
                print("\n--- Lista de Clientes ---")
                servicio.listar_clientes()

            elif opcion == "6":
                print("\n--- Buscar Cliente ---")
                id_buscar = input("Ingrese el ID del cliente a buscar: ")
                servicio.buscar_cliente(id_buscar)

            elif opcion == "7":
                print("\nSaliendo del sistema...")
                break
            else:
                print("Opción inválida. Intente de nuevo.")

        except ValueError as e:
            print(f"Error de validación: {e}")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")


if __name__ == "__main__":
    ejecutar_sistema()