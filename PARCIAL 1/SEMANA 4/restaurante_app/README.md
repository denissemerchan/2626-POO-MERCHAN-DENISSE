# Sistema de Gestión de Restaurante / Sabor Ecuatoriano

**Estudiante:**
Denisse Margarita Merchan Jauregui

## Descripción del Sistema
Este es un sistema básico para simular la gestión de un restaurante. Permite registrar diferentes productos del menú y almacenar los datos de los clientes que consumen en el establecimiento, controlando toda la información desde un programa centralizado.

## Estructura del Proyecto
El programa se encuentra organizado bajo los siguientes archivos:
- `modelos/producto.py`: Define la clase Producto con sus atributos básicos (nombre y precio).
- `modelos/cliente.py`: Define la clase Cliente con sus datos de identificación.
- `servicios/restaurante.py`: Gestiona las listas de productos y clientes registrados.
- `main.py`: Punto de entrada del programa donde se situan los objetos y se realiza la ejecucion del programa.

## Reflexión sobre la Modularidad
La importancia de la modularización es que permite separar de forma clara las responsabilidades de cada componente de software. Al segmentar los modelos de datos de la lógica de negocio o servicios, el código se vuelve mucho más legible, fácil de mantener y escalable ante futuros requerimientos.