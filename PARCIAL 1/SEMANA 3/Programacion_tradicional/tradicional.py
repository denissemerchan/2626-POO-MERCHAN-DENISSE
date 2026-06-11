print("Hola, por favor ingrese los datos de su mascota:")
# Función para registrar mascota
def registrar_mascota():
    nombre = input("Nombre: ")
    especie = input("Especie: ")
    edad = input("Edad: ")
    return {"nombre": nombre, "especie": especie, "edad": edad}

# Función para mostrar datos
def mostrar_mascota(mascota):
    print(f"\nMascota: {mascota['nombre']}, Especie: {mascota['especie']}, Edad: {mascota['edad']}")

# Ejecución principal
print("Registro Tradicional")
m1 = registrar_mascota()
mostrar_mascota(m1)