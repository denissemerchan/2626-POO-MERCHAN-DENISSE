# Proyecto Restaurante App - Semana 9

## Estudiante
DENISSE MARGARITA MERCHAN JAUREGUI

## Descripción del Sistema
Aplicación modular desarrollada para consola que facilita la gestión organizada de productos y usuarios en un restaurante, 
empleando estructuras de datos fundamentales en Python.

## Estructura del Proyecto
- `modelos/`: Guarda la definición de las clases principales (`producto.py`, `usuario.py`).
- `servicios/`: Alberga el servicio con las operaciones y manejo de registros (`restaurante.py`).
- `main.py`: Funciona como interfaz de consola e integra los flujos de trabajo.

## Aplicación de Estructuras de Datos
- **Listas (list):** Almacenan de forma dinámica la colección de registros de `Producto` y `Usuario`.
- **Tuplas (tuple):** Guardan las opciones del menú principal para asegurar que no sufran alteraciones.
- **Diccionarios (dict):** Relacionan de manera lógica las claves de selección con los servicios disponibles.
- **Conjuntos (set):** Extraen automáticamente las categorías de los productos asegurando que no existan duplicados.

## Instrucciones de Ejecución
1. Abrir una consola de comandos dentro de la carpeta `restaurante_app/`.
2. Ejecutar la aplicación con el comando: `python main.py`

## Reflexión sobre la Elección de Estructuras de Datos
Seleccionar la estructura de datos apropiada es esencial para construir programas eficientes, seguros y fáciles de entender. 
El empleo de **listas** brinda la elasticidad requerida en arreglos de elementos que crecen continuamente. En contraste, 
las **tuplas** resguardan la integridad de información fija, impidiendo cambios indeseados durante la ejecución.
Por otro lado, los **diccionarios** agilizan la localización de datos conectando claves con sus valores correspondientes, 
mientras que los **conjuntos** aíslan elementos únicos sin requerir algoritmos complejos de verificación. Aplicar cada 
colección de acuerdo a sus fortalezas específicas reduce el consumo innecesario de recursos y contribuye a la solidez del proyecto.