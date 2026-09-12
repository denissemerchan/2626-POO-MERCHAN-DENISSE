# restaurante_app - Semana 13 - Interfaz Gráfica con Tkinter

## Descripción
Se presenta la versión inicial con interfaz gráfica para `restaurante_app`, desarrollada a partir de la estructura modular base del repositorio docente. Esta entrega incorpora un módulo de inicio de sesión simulado y permite la lectura de información sobre productos y usuarios almacenada en archivos JSON locales.

## Estructura del Proyecto
```text
restaurante_app/
│── datos/
│   ├── productos.json
│   └── usuarios.json
│── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
│── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
│── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
│── main.py
└── README.md
```

## Flujo de la Aplicación

1. `main.py` inicializa la ventana principal de Tkinter y carga los servicios.

2. Muestra la pantalla de login (`LoginView`).

3. Tras validar las credenciales con `RestauranteServicio`, cambia a la pantalla principal (`MainView`) dentro de la misma ventana.

4. Permite consultar listas de Productos y Usuarios. La opción Ventas muestra una notificación de funcionalidad pendiente.

5. Al hacer clic en Cerrar sesión, destruye la vista actual y retorna al login.

## Ejecución

### 1. Requisitos Previos
* Python 3.8 o superior instalado.
* No se requieren librerías externas de terceros (se utilizan módulos nativos como `tkinter`, `json` y `os`).

### 2. Archivos de Datos (`.json`)
La aplicación utiliza archivos JSON (`productos.json` y `usuarios.json`) para la persistencia de datos. 

* Si los archivos no existen al iniciar el programa por primera vez, la aplicación los creará automáticamente con una estructura base vacía.
* Si deseas iniciar con datos de prueba, asegúrate de tener creados los archivos en la raíz del proyecto con la siguiente estructura:

**`usuarios.json`**
```json
[
  {
    "identificador": "U001",
    "nombre": "Administrador",
    "usuario": "admin",
    "contrasena": "1234"
  }
]
```

### 3. Pasos para Ejecutar

1. Abre tu terminal o consola de comandos en la carpeta raíz del proyecto.

2. Ejecuta el archivo principal mediante el siguiente comando:

`python main.py`

- Inicia sesión con las credenciales configuradas en tu archivo `usuarios.json`.