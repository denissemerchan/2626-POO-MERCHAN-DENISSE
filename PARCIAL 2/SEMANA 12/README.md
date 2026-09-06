# Restaurante App - Semana 12

## Estudiante:
**DENISSE MARGARITA MERCHAN JAUREGUI** 

## Descripción del Proyecto
Implementación de estructuras auxiliares basadas en diccionarios para `restaurante_app`, mejorando el rendimiento general de la aplicación al reducir los tiempos de respuesta en las búsquedas y consultas recurrentes.

## Estructura del Proyecto
```text
restaurante_app/
│── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
│── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
│── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
│── main.py
└── README.md
```

## Mejoras de Rendimiento Aplicadas  
Se conservaron las listas principales (`_productos, _usuarios, _ventas`) para mantener el orden y la persistencia en archivos JSON, e incorporamos índices auxiliares en memoria (`dict`):

_Búsqueda de productos (`buscar_producto`):_

Antes: Recorrido lineal O(n) sobre la lista de productos.

Ahora: Búsqueda instantánea O(1) usando el diccionario `_index_productos`.

_Búsqueda de usuarios (`buscar_usuario`):_

Antes: Recorrido lineal O(n) sobre la lista de usuarios.

Ahora: Búsqueda instantánea O(1) usando el diccionario `_index_usuarios`.

_Consulta de ventas por usuario (`consultar_ventas_usuario`):_

Antes: Filtro lineal O(n) recorriendo todas las ventas registradas.

Ahora: Consulta instantánea O(1) usando la estructura `_index_ventas_usuario` (dict de `id_usuario` -> `List[Venta]`).

_Sincronización y Reconstrucción_

Reconstrucción inicial: Al iniciar el programa, el método `_reconstruir_indices()` llena los diccionarios a partir de los datos recuperados desde JSON.

Sincronización continua: Cada vez que se registra un nuevo producto, usuario o venta, la información se añade tanto a la lista de persistencia como al índice auxiliar correspondiente.

## Estructuras Utilizadas
- `self.productos` / `self.usuarios` / `self.ventas`: Listas para almacenamiento persistente y recorrido global.
- `self._index_productos`: `dict` `[codigo -> Producto]`
- `self._index_usuarios`: `dict` `[identificacion -> Usuario]`
- `self._index_ventas_usuario`: `dict` `[id_usuario -> List[Venta]]`

## Ejecución

python main.py

## Validación y Pruebas

* **Persistencia Básica:** Registro de entidades iniciales, cierre forzado y reanudación del programa para validar el restablecimiento correcto de la información.
* **Procesamiento de Venta Aceptada:** Se procesó la compra de 20 unidades sobre un ítem con 30 existencias. Se confirmó la reducción del saldo a 10 unidades, la adición del objeto en `ventas.json` y su vinculación con la cuenta correspondiente.
* **Procesamiento de Venta Rechazada:** Se intentó solicitar un volumen de productos superior al disponible. La operación fue denegada de forma segura sin alterar las colecciones ni los archivos.
* **Filtro de Historial:** Consulta del historial de transacciones por identificación de usuario, asegurando el filtrado e iteración adecuada sobre la lista de ventas.