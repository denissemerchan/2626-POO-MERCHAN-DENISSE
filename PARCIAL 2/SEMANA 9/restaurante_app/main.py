from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.usuario import Usuario


def ejecutar_sistema() -> None:
    restaurante = Restaurante()

    # Tupla para las opciones estables del menú principal
    opciones_menu: tuple = (
        "1. Registrar producto",
        "2. Buscar producto",
        "3. Actualizar producto",
        "4. Eliminar producto",
        "5. Listar productos",
        "6. Registrar usuario",
        "7. Listar usuarios",
        "8. Mostrar categorías",
        "9. Salir"
    )

    while True:
        print("\n==============================")
        print("     SISTEMA DE RESTAURANTE")
        print("==============================")
        for opcion in opciones_menu:
            print(opcion)

        try:
            opcion_elegida: str = input("\nSeleccione una opción: ").strip()

            if opcion_elegida == "1":
                codigo = input("Código: ").strip()
                nombre = input("Nombre: ").strip()
                categoria = input("Categoría: ").strip()
                precio = float(input("Precio: "))

                nuevo_prod = Producto(codigo, nombre, categoria, precio)
                if restaurante.registrar_producto(nuevo_prod):
                    print("¡Producto registrado con éxito!")
                else:
                    print("Error: El código ya existe.")

            elif opcion_elegida == "2":
                codigo = input("Código a buscar: ").strip()
                prod = restaurante.buscar_producto(codigo)
                if prod:
                    print(f"Encontrado -> {prod.nombre} | ${prod.precio} | {prod.categoria}")
                else:
                    print("Producto no encontrado.")

            elif opcion_elegida == "3":
                codigo = input("Código del producto a actualizar: ").strip()
                nombre = input("Nuevo nombre: ").strip()
                categoria = input("Nueva categoría: ").strip()
                precio = float(input("Nuevo precio: "))

                if restaurante.actualizar_producto(codigo, nombre, categoria, precio):
                    print("¡Producto actualizado!")
                else:
                    print("Producto no encontrado.")

            elif opcion_elegida == "4":
                codigo = input("Código a eliminar: ").strip()
                if restaurante.eliminar_producto(codigo):
                    print("¡Producto eliminado!")
                else:
                    print("Producto no encontrado.")

            elif opcion_elegida == "5":
                print("\n--- LISTA DE PRODUCTOS ---")
                if not restaurante.lista_productos:
                    print("No hay productos registrados.")
                for p in restaurante.lista_productos:
                    print(f"[{p.codigo}] {p.nombre} - {p.categoria} - ${p.precio}")

            elif opcion_elegida == "6":
                iden = input("Identificación: ").strip()
                nombre = input("Nombre: ").strip()
                correo = input("Correo: ").strip()

                nuevo_usu = Usuario(iden, nombre, correo)
                if restaurante.registrar_usuario(nuevo_usu):
                    print("¡Usuario registrado con éxito!")
                else:
                    print("Error: La identificación ya existe.")

            elif opcion_elegida == "7":
                print("\n--- LISTA DE USUARIOS ---")
                if not restaurante.lista_usuarios:
                    print("No hay usuarios registrados.")
                for u in restaurante.lista_usuarios:
                    print(f"[{u.identificacion}] {u.nombre} - {u.correo}")

            elif opcion_elegida == "8":
                print("\n--- CATEGORÍAS ÚNICAS ---")
                cats = restaurante.obtener_categorias()
                if not cats:
                    print("No hay categorías registradas.")
                for c in cats:
                    print(f"- {c}")

            elif opcion_elegida == "9":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción inválida. Intente de nuevo.")

        except ValueError:
            print("Error: Ingrese valores numéricos correctos donde corresponda.")


if __name__ == "__main__":
    ejecutar_sistema()