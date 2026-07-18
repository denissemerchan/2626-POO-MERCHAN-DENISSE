# Sistema Restaurante App

**Estudiante:** Denisse Margarita Merchan Jauregui
**Asignatura:** Programación Orientada a Objetos - Semana 8  

## Descripción del sistema
Este proyecto consiste en una aplicación modular de consola en Python diseñada para gestionar productos, bebidas y 
clientes de un restaurante, aplicando principios SOLID de diseño de software.

## Estructura del proyecto
```text
restaurante_app/
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── bebida.py
│   └── cliente.py
│
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
│
├── main.py
└── README.md
```
## Responsabilidad de cada clase
Producto (modelos/producto.py): Clase base encargada puramente de representar los datos comunes de un producto del 
restaurante y mostrar su información.

Bebida (modelos/bebida.py): Clase hija que especializa a Producto añadiendo atributos específicos (tamano y tipo_envase).

Cliente (modelos/cliente.py): Clase independiente encargada de modelar la información y los datos de un cliente registrado.

Restaurante (servicios/restaurante.py): Clase de servicio encargada de controlar el negocio interno: almacenamiento, 
validación de duplicados y listado estructurado de colecciones.

Main (main.py): Punto de entrada del programa. Coordina el menú, captura datos por consola mediante input() e interactúa 
directamente con el servicio.

## Principios SOLID aplicados
Single Responsibility Principle (SRP): Cada clase tiene una única razón para cambiar. Los modelos guardan datos, el 
servicio administra la lógica de negocio y main.py maneja la interfaz por consola.

Open/Closed Principle (OCP): El sistema permite la extensión mediante herencia al incorporar Bebida sin alterar la 
estructura interna de Producto ni forzar reescrituras críticas en el servicio principal.

Liskov Substitution Principle (LSP): La clase Bebida hereda correctamente de Producto, permitiendo que el listado de 
productos procese de forma transparente y polimórfica objetos de ambos tipos mediante el método unificado mostrar_informacion().