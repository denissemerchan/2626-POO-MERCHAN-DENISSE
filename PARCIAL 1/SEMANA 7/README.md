# Sistema de Gestión de Restaurante (Semana 7 - POO)

**Estudiante:** Denisse MArgarita Merchan Jauregui
**Asignatura:** Programación Orientada a Objetos  
**Semana:** 7

---

## 1. Descripción del Sistema
Este sistema es una aplicación de consola modular en Python diseñada para gestionar los productos y clientes de un restaurante. 
Permite registrar dinámicamente nuevos elementos, listar la información guardada en memoria y realizar búsquedas específicas 
mediante un menú interactivo. El objetivo principal es aplicar los conceptos de modularidad, encapsulamiento, clases de datos 
y el flujo correcto desde la entrada de datos por consola hasta la persistencia temporal en objetos de servicio.

---

## 2. Estructura del Proyecto
El proyecto sigue una arquitectura modular por capas para separar las entidades de datos de la lógica de negocio:

```text
restaurante_app/
│
├── modelos/
│   ├── __init__.py          # Inicializador del paquete de modelos
│   ├── producto.py          # Clase Producto (Encapsulamiento tradicional)
│   └── cliente.py           # Clase Cliente (Dataclass)
│
├── servicios/
│   ├── __init__.py          # Inicializador del paquete de servicios
│   └── restaurante.py       # Clase Servicio (Gestión de listas y lógica)
│
└── main.py                  # Punto de arranque e interfaz de usuario
```
## 3. Componentes Principales y Uso de POO
**Uso del Constructor en la Clase Producto**
La clase Producto utiliza el constructor tradicional de Python __init__(). Al instanciar un objeto, los valores recibidos se asignan 
directamente a través de sus propiedades. Esto garantiza que cualquier dato entrante pase obligatoriamente por los filtros de validación 
antes de ser asignado a los atributos privados simulados (_nombre, _categoria, _precio).

**Uso de @property y @setter**
-Se implementó el encapsulamiento en la clase Producto utilizando los decoradores @property (para la lectura controlada) y @setter 
(para la asignación y validación).
-Evitan que los atributos críticos sean modificados directamente con valores no válidos.
-Llevan a cabo validaciones obligatorias: los campos nombre y categoria no pueden estar vacíos o con espacios en blanco, y el precio 
debe ser estrictamente mayor que cero (> 0).

**Uso de @dataclass en la Clase Cliente**
Para la clase Cliente se empleó el decorador @dataclass del módulo nativo de Python. Esto reduce drásticamente el código repetitivo 
(boilerplate), ya que genera de forma automática el constructor __init__(), la representación legible __repr__() y los métodos de 
comparación, permitiendo un modelado de datos limpio y directo para atributos básicos como nombre, correo e id_cliente.

## 4. Descripción del Menú Interactivo
La interfaz de usuario corre en main.py mediante un ciclo continuo (while True) que despliega el siguiente menú:
-Registrar producto: Solicita nombre, categoría y precio, valida los tipos de datos y crea el objeto.
-Listar productos: Muestra de forma legible en consola todos los productos almacenados.
-Buscar producto: Permite encontrar productos filtrando por coincidencia parcial en el nombre.
-Registrar cliente: Pide el nombre, correo electrónico e ID único para guardarlo.
-Listar clientes: Imprime todos los registros de clientes en el sistema.
-Buscar cliente: Localiza un cliente específico mediante la coincidencia exacta de su ID.
-Salir: Rompe el ciclo del programa y finaliza la ejecución con seguridad.

## 5. Reflexión sobre la Creación de Objetos desde Consola
Crear objetos a partir de datos ingresados dinámicamente por el usuario, en lugar de usar datos quemados (hardcoded) en el código, 
es un paso fundamental para construir aplicaciones reales, flexibles y útiles, este flujo permite entender cómo la programación 
orientada a objetos interactúa con el mundo exterior: la información sin procesar provista por el usuario pasa por una capa de 
validación, se moldea bajo una estructura segura dentro de un constructor y se convierte en una entidad lógica con comportamiento 
propio. Esta abstracción permite que el software sea verdaderamente interactivo y capaz de adaptarse a cualquier entrada en tiempo 
de ejecución.