# Restaurante App - Semana 6

**Estudiante:** DENISSE MARGARITA MERCHAN JAUREGUI

## Descripción
Este sistema modular en Python simula la gestión de productos en un restaurante aplicando los pilares de la Programación Orientada a Objetos (POO).

## Principios de POO Aplicados
* **Herencia:** Las clases `Platillo` y `Bebida` heredan de la clase padre `Producto`.
* **Encapsulación:** El atributo `__precio` es privado en `Producto` y se controla mediante `obtener_precio()` y `cambiar_precio()` con validaciones.
* **Polimorfismo:** El método `mostrar_informacion()` se sobrescribe en las clases hijas y se ejecuta dinámicamente en el servicio `Restaurante`.

## Reflexión sobre el uso de POO en Proyectos Modulares
La aplicación de los principios de POO en proyectos modulares de Python es fundamental para el desarrollo de software profesional. La herencia elimina la duplicación de código al reutilizar estructuras comunes, 
mientras que la encapsulación protege los datos sensibles frente a modificaciones no autorizadas desde el exterior. Finalmente, el polimorfismo permite tratar de forma genérica colecciones de objetos diversos, 
facilitando la escalabilidad del sistema. En conjunto, estos pilares organizados en módulos independientes garantizan un código limpio, ordenado y sumamente fácil de mantener o expandir a futuro.