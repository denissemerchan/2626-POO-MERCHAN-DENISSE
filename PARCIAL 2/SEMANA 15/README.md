# Sistema de Gestión de Restaurante - Semana 15

## Propósito de la Semana 15
El objetivo principal de esta semana es implementar el **manejo de eventos** en entornos gráficos utilizando Tkinter/ttk. La arquitectura del proyecto evoluciona para incorporar un módulo de **Gestión de Ventas**, demostrando cómo la interfaz gráfica reacciona a las acciones del usuario mediante `command=` y *callbacks*, delegando la lógica de negocio y persistencia a la capa de servicios sin sobrecargar la vista.

## Evolución del Proyecto
A partir de la versión base desarrollada en semanas anteriores, se han realizado las siguientes mejoras y adiciones:
1. **Nuevas Entidades y Modelos**: Incorporación de la clase `Venta` en la capa de modelos.
2. **Modulo de Ventas en la UI**: Integración de una nueva sección en el panel principal (`MainView`) con desplegables (`ttk.Combobox`) para asociar usuarios y productos.
3. **Persistencia de Ventas**: Extensión de la capa de almacenamiento para registrar y leer datos de ventas de forma persistente.
4. **Recursos Visuales**: Integración de íconos corporativos y mejor escalado de imágenes en la barra lateral y botones mediante la carpeta `assets/`.

## Estructura del Sistema

La aplicación mantiene su arquitectura modular en capas:

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
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── assets/
├── main.py
└── README.md
```

## Nueva Gestión de Ventas
La nueva pantalla de **Ventas** permite registrar transacciones en tiempo real:
* **Selección de Usuario**: Desplegable que obtiene los usuarios activos del sistema (`identificador - nombre`).
* **Selección de Producto**: Desplegable que obtiene los platillos/productos disponibles (`codigo - nombre`).
* **Tabla de Historial**: Un `ttk.Treeview` que muestra el ID de la venta, el usuario comprador, el producto adquirido y la fecha de registro.

## Uso de `command=` y Callbacks (Manejo de Eventos)

El flujo de interacción sigue el patrón desacoplado de eventos de Tkinter:

```text
[ Acción del Usuario ]
         │
         ▼ (Clic en botón)
[ Evento Tkinter ] ────► command = self.registrar_venta
         │
         ▼
[ Callback ] ──────────► Obtiene valores del Combobox
         │
         ▼
[ Servicio ] ──────────► RestauranteServicio.registrar_venta(...)
         │              (Aplica validaciones de negocio)
         ▼
[ Persistencia ] ──────► ArchivoServicio guarda en ventas.json
         │
         ▼
[ Respuesta UI ] ──────► Refresco del Treeview + MessageBox de éxito
```

1. **Configuración del Botón**: Se asigna el callback al parámetro `command`:
   ```python
   self.crear_boton(
       acciones,
       "Registrar venta",
       self.registrar_venta,  # Callback desencadenado
       "Accion.TButton",
       "add.png"
   )
   ```
2. **Ejecución del Callback (`self.registrar_venta`)**: Captura los valores de la interfaz, los procesa y delega la operación al servicio `restaurante_servicio`.
3. **Respuesta en la UI**: Tras procesarse en el servicio, la interfaz invoca `self.refrescar_ventas()` y muestra un mensaje al usuario sin congelar la vista.

## Persistencia en `ventas.json`

Las ventas se almacenan de manera estructurada dentro de `datos/ventas.json`. El archivo mantiene un formato JSON legible:

```json
[
  {
    "identificador": "V001",
    "usuario_id": "U001",
    "producto_codigo": "P001",
    "fecha": "2026-09-24"
  }
]
```

`ArchivoServicio` gestiona la lectura y escritura automática de este archivo, permitiendo que la información perdure entre reinicios de la aplicación.

## Pasos para Ejecutar la Aplicación

### Requisitos Previos
* Python 3.8 o superior instalado.
* Tkinter (incluido por defecto en la instalación estándar de Python).

### Instrucciones de Ejecución

1. Ejecute el punto de entrada principal:
   ```bash
   python main.py
   ```

2. Inicie sesión con un usuario válido para acceder al panel principal y navegar hacia la sección de **Ventas**.
_Credenciales validas:_

Administrador:
   - Usuario: `admin`
   - Contraseña: `1234`
   
Mesera Ana:
   - Usuario: `Ana`
   - Contraseña: `abcd`
