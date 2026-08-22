from servicios.restaurante import Restaurante
from servicios.archivo_servicio import ArchivoServicio
from modelos.producto import Producto


def menu() -> None:
    archivo_servicio = ArchivoServicio()
    restaurante = Restaurante()

    productos_cargados = archivo_servicio.cargar_productos()
    restaurante.establecer_productos(productos_cargados)

    while True:
        print("\n--- SISTEMA DE RESTAURANTE ---")
        print("1. Listar productos")
        print("2. Registrar producto")
        print("3. Buscar producto")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            prods = restaurante.obtener_productos()
            if not prods:
                print("No hay productos registrados.")
            else:
                for p in prods:
                    print(p)

        elif opcion == "2":
            try:
                id_prod = int(input("Ingrese el ID del producto: "))
                nombre = input("Ingrese el nombre del producto: ")
                precio = float(input("Ingrese el precio del producto: "))

                nuevo_p = Producto(id_prod, nombre, precio)
                if restaurante.registrar_producto(nuevo_p):
                    archivo_servicio.guardar_productos(restaurante.obtener_productos())
                    print("Producto registrado y guardado exitosamente.")
            except ValueError as e:
                print(f"[Error de validación]: {e}")

        elif opcion == "3":
            try:
                id_prod = int(input("Ingrese el ID a buscar: "))
                prod = restaurante.buscar_producto_por_id(id_prod)
                if prod:
                    print(prod)
                else:
                    print("Producto no encontrado.")
            except ValueError:
                print("[Error] El ID debe ser un número entero.")

        elif opcion == "4":
            try:
                id_prod = int(input("Ingrese el ID del producto a actualizar: "))
                if restaurante.buscar_producto_por_id(id_prod) is None:
                    print("El producto no existe.")
                    continue
                nombre = input("Ingrese el nuevo nombre: ")
                precio = float(input("Ingrese el nuevo precio: "))

                if restaurante.actualizar_producto(id_prod, nombre, precio):
                    archivo_servicio.guardar_productos(restaurante.obtener_productos())
                    print("Producto actualizado y guardado exitosamente.")
            except ValueError as e:
                print(f"[Error de validación]: {e}")

        elif opcion == "5":
            try:
                id_prod = int(input("Ingrese el ID del producto a eliminar: "))
                if restaurante.eliminar_producto(id_prod):
                    archivo_servicio.guardar_productos(restaurante.obtener_productos())
                    print("Producto eliminado y guardado exitosamente.")
                else:
                    print("Producto no encontrado.")
            except ValueError:
                print("[Error] El ID debe ser un número entero.")

        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    menu()