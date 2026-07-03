# Restaurante App - Semana 6

**Estudiante:** DENISSE MARGARITA MERCHAN JAUREGUI

## Descripción
Este sistema modular en Python simula la gestión de productos en un restaurante aplicando los pilares de la Programación Orientada a Objetos (POO).

## Principios de POO Aplicados
* **Herencia:** Las clases `Platillo` y `Bebida` heredan de la clase padre `Producto`.
* **Encapsulación:** El atributo `__precio` es privado en `Producto` y se controla mediante `obtener_precio()` y `cambiar_precio()` con validaciones.
* **Polimorfismo:** El método `mostrar_informacion()` se sobrescribe en las clases hijas y se ejecuta dinámicamente en el servicio `Restaurante`.