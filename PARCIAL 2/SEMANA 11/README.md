# Aplicación Restaurante - Entrega Semana 11

## Datos del Estudiante:
**DENISSE MARGARITA MERCHAN JAUREGUI**

## Resumen del Proyecto
El programa `restaurante_app` es una solución en Python diseñada para simular la operación lógica de un restaurante. En este avance, la arquitectura incorpora la clase `Venta` para relacionar clientes con artículos, permitiendo rastrear el inventario en tiempo real y asegurar la persistencia de información mediante archivos en formato JSON.

## Organización del Código
```text
restaurante_app/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── main.py
└── README.md

```

## Distribución de Responsabilidades

* `modelos/producto.py`: Contiene la entidad `Producto`, sus reglas de encapsulamiento, el manejo del inventario (`stock`) y las funciones necesarias para transformar los objetos a estructuras compatibles con JSON y viceversa.
* `modelos/usuario.py`: Modela la entidad `Usuario` y garantiza la validez de las identificaciones y nombres ingresados.
* `modelos/venta.py`: Estructura el registro del intercambio entre `Usuario` y `Producto` guardando `usuario_id`, `producto_codigo` y la `cantidad`.
* `servicios/archivo_servicio.py`: Centraliza las operaciones de lectura y escritura en el almacenamiento secundario (`productos.json`, `usuarios.json`, `ventas.json`) apoyándose en la librería estándar mediante `json.dump()` y `json.load()`.
* `servicios/restaurante.py`: Administra las colecciones en memoria, ejecuta la lógica del negocio (verificación de existencia, decremento de existencias, filtrado de historial) y solicita la sincronización en disco.
* `main.py`: Funciona como la interfaz de línea de comandos (CLI) que captura la entrada del usuario y delega el procesamiento al servicio principal.

## Flujo de Operación de Ventas y Control de Stock

Cada elemento del catálogo gestiona sus unidades disponibles (`stock`). Durante una transacción:

* El sistema confirma la presencia previa del usuario y del producto solicitado.
* Se valida que la cantidad requerida sea un entero positivo y no sobrepase el stock disponible.
* Se genera la instancia `Venta` asociando las claves primarias de ambas entidades.
* Se invoca el método `vender()` para restar las unidades correspondientes del catálogo.
* Se actualizan inmediatamente los datos en los archivos JSON correspondientes.

## Almacenamiento Persistente

La sincronización con los archivos es automática ante cualquier cambio:

* Registro de nuevo usuario: Escribe en `usuarios.json`.
* Creación de nuevo producto: Escribe en `productos.json`.
* Procesamiento de venta: Actualiza en paralelo `ventas.json` y `productos.json`.
* Inicio de la aplicación: Lee los ficheros dentro del directorio `datos/` y reconstruye los objetos en memoria.

## Control de Excepciones

* `FileNotFoundError`: Garantiza que el sistema inicie con colecciones vacías si no se ubican los archivos JSON.
* `json.JSONDecodeError`: Captura anomalías en la lectura de archivos con sintaxis JSON corrupta.
* `PermissionError`: Previene fallos críticos por restricciones de permisos en el sistema de archivos.
* `KeyError`: Se activa si los diccionarios recuperados carecen de los atributos esperados.
* `ValueError`: Rechaza el procesamiento de datos numéricos o textos con formatos incorrectos.

## Instrucciones de Uso

Para iniciar el sistema, ejecute desde el directorio raíz:`python main.py`

## Validación y Pruebas

* **Persistencia Básica:** Registro de entidades iniciales, cierre forzado y reanudación del programa para validar el restablecimiento correcto de la información.
* **Procesamiento de Venta Aceptada:** Se procesó la compra de 20 unidades sobre un ítem con 120 existencias. Se confirmó la reducción del saldo a 100 unidades, la adición del objeto en `ventas.json` y su vinculación con la cuenta correspondiente.
* **Procesamiento de Venta Rechazada:** Se intentó solicitar un volumen de productos superior al disponible. La operación fue denegada de forma segura sin alterar las colecciones ni los archivos.
* **Filtro de Historial:** Consulta del historial de transacciones por identificación de usuario, asegurando el filtrado e iteración adecuada sobre la lista de ventas.
