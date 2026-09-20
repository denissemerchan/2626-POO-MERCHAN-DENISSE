# Restaurante App - Semana 14

**Estudiante:** DENISSE MARGARITA MERCHAN JAUREGUI

## Descripción del Proyecto
Evolución del proyecto `restaurante_app` correspondiente a la Semana 14. Se mejoró la interfaz gráfica incorporando contenedores (`Notebook`, `LabelFrame`, `Frame`) y componentes organizados (`Treeview`, `Combobox`, `Entry`, `Button`), manteniendo la arquitectura modular en capas y la persistencia de datos mediante archivos JSON.

## Estructura del Proyecto
```text
restaurante_app/
├── datos/
│   ├── productos.json
│   └── usuarios.json
├── modelos/
│   ├── init.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── init.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── init.py
│   ├── login_view.py
│   └── main_view.py
├── assest/
├── main.py
└── README.md
```

## Componentes y Contenedores Utilizados
- **Contenedores:** 
  - `Notebook`: Para dividir la interfaz en pestañas ("Gestión de Productos" y "Consulta de Usuarios").
  - `LabelFrame` y `Frame`: Para agrupar de forma ordenada el formulario de entrada y la tabla de resultados.
- **Componentes:**
  - `Treeview`: Tabla para listar productos y usuarios con barra de desplazamiento (`Scrollbar`).
  - `Combobox`: Menú desplegable para seleccionar categorías de productos.
  - `Entry` y `Button`: Formularios y botones vinculados mediante `command=`.

## Operaciones de Productos Implementadas
1. **Registrar:** Añade un nuevo producto validando campos requeridos y tipos de datos en el servicio.
2. **Cargar/Consultar:** Busca por ID y llena el formulario con los datos encontrados.
3. **Actualizar:** Modifica la información del producto consultado.
4. **Eliminar:** Remueve el producto seleccionado mediante su ID.
5. **Listar:** Muestra todos los productos registrados dentro de una tabla interactiva (`ttk.Treeview`).

## Persistencia utilizada
La persistencia de datos se maneja de forma local mediante archivos **JSON**:
* Los datos se almacenan en la carpeta `datos/` (`productos.json` y `usuarios.json`).
* Se utiliza la clase `ArchivoServicio` para realizar las lecturas y escrituras en disco, garantizando que la información se conserve al cerrar y reabrir la aplicación.

## Instrucciones de Ejecución
1. Abrir una terminal en el directorio del proyecto.
2. Ejecutar el archivo principal:
   ```bash
   python main.py
    ```
3. Utilizar la siguiente credencial de acceso: 
    - Usuario: `admin`
    - Contraseña: `1234`
