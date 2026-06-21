class Restaurante:
    def __init__(self, nombre):
        #Inicializa el nombre y las listas vacías
        self.nombre = nombre
        self.productos = []
        self.clientes = []

    def registrar_producto(self, producto):
        #Agrega un producto a la lista
        self.productos.append(producto)
        print(f"✔ Producto registrado: {producto.nombre}")

    def registrar_cliente(self, cliente):
        #Agrega un cliente a la lista
        self.clientes.append(cliente)
        print(f"✔ Cliente registrado: {cliente.nombre}")

    def mostrar_informacion(self):
        #Muestra lo guardado en la consola
        print(f"\n=== SISTEMA: {self.nombre.upper()} ===")

        print("\n--- MENÚ ---")
        for prod in self.productos:
            print(prod)

        print("\n--- CLIENTES ---")
        for cli in self.clientes:
            print(cli)
        print("=" * 40)