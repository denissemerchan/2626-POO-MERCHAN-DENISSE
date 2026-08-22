# Sistema de Gestión de Restaurante - POO

## Estudiante:
Denisse Margarita Merchan Jauregui

## Descripción del Sistema
La aplicación es un sistema de consola desarrollado en Python para administrar el inventario de un restaurante. Permite 
registrar, buscar, actualizar, listar y eliminar productos del menú, garantizando la persistencia de los datos mediante 
almacenamiento en archivos JSON.

## Estructura del Proyecto

```text
restaurante_app/
│
├── datos/
│   └── productos.json
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
│
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
│
├── main.py
└── README.md
```
## Responsabilidad de Componentes
1. `modelos/producto.py`: Define la clase Producto con encapsulamiento mediante decoradores `@property` para validar que los
IDs sean enteros positivos, los nombres no estén vacíos y los precios sean mayores a cero.
2. `modelos/usuario.py`: Modela los datos de los usuarios del sistema.
3. `servicios/restaurante.py`: Administra la lógica de negocio del sistema (lista, almacena en memoria, actualiza y elimina 
productos).
4. `servicios/archivo_servicio.py`: Controla la lectura y escritura persistente del archivo JSON.
5. `main.py`: Punto de entrada del programa; presenta el menú interactivo para interactuar con el usuario.

## Funcionamiento de productos.json
El archivo `datos/productos.json` actúa como la base de datos del sistema. Guarda los productos en formato JSON como una 
lista de diccionarios, manteniendo la información estructurada mediante claves (`id_producto, nombre, precio`).

## Flujo de Carga y Guardado
1. Carga Inicial: Al iniciar el programa, `ArchivoServicio.cargar_productos()` lee el archivo JSON, convierte cada registro 
en una instancia de la clase Producto y los carga en la memoria del sistema (Restaurante).
2. Guardado en Tiempo Real: Cada vez que se registra, actualiza o elimina un producto, el método `guardar_productos()` 
convierte los objetos `Producto` nuevamente a diccionarios y sobrescribe el archivo JSON.

## Excepciones Controladas
1. `FileNotFoundError`: Captura la ausencia del archivo de datos e inicia el sistema con una lista vacía.
2. `JSONDecodeError`: Evita que el programa falle si el archivo JSON está corrupto o mal formado.
3. `PermissionError`: Controla los errores de acceso o falta de permisos al leer/escribir en el disco.
4. `ValueError`: Captura errores de entrada de datos por parte del usuario (como ingresar texto en un campo de número o 
intentar registrar precios negativos).

## Instrucciones de Ejecución
1. Abrir la carpeta del proyecto `restaurante_app` en el entorno de desarrollo (PyCharm).
2. Verificar que Python 3.10 o superior esté seleccionado.
3. Ejecutar el archivo principal desde la consola o IDE: `python main.py`.

## Comprobación de Persistencia de Datos
1. Para verificar que los productos permanecen guardados después de cerrar la aplicación, se realizaron los siguientes pasos:
2. Se ejecutó `main.py` y se registró un nuevo producto.
3. Se cerró la aplicación mediante la opción de salir del menú.
4. Se verificó visualmente que la información quedó registrada dentro del archivo `datos/productos.json`.
5. Se volvió a ejecutar `main.py` y se seleccionó la opción de listar productos, comprobando que la información ingresada 
se cargó automáticamente en pantalla.