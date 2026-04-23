# 2do Parcial - Análisis de Datos de Netflix con Interfaz Gráfica

Esta carpeta contiene la implementación del proyecto del **Segundo Parcial**, el cual consiste en un sistema con interfaz gráfica profesional, desarrollado en Python, para realizar consultas y análisis complejos a un _dataset_ (.csv).

## Arquitectura del Proyecto

Para la realización del proyecto se ha decidido organizar el código de manera modular en lugar de concentrar todo en un solo script:

- **`main.py`**: Es el archivo principal que inicializa los temas de color global para CustomTkinter y lanza el sistema. Ejecuta este archivo para probar la app.
- **`data/`**: Directorio de almacenamiento.
  - `netflix_titles.csv`: La base de datos cruda del análisis de pandas.
  - `usuarios.txt`: La base de datos simulada con las credenciales, en formato `usuario:contraseña`.
- **`login_gui.py`**: Interfaz de inicio de sesión de CustomTkinter que lee `usuarios.txt` para validar accesos, gestionando errores visualmente.
- **`app_gui.py`**: Maneja el layout principal. Un marco (frame) a la izquierda actúa de menú para las 10 consultas; un marco derecho presenta una tabla de datos (vía `ttk.Treeview`) adaptada al modo oscuro.
- **`queries.py`**: Toda la lógica robusta de manipulación de datos usando `Pandas`. Al pulsar un botón de la GUI, en este módulo la base de datos se limpia, pivotea, agrupa o expone datos, y retorna junto con la justificación solicitada.

## Flujo de Trabajo y Funcionalidad Destacada

1. **CustomTkinter**: La apariencia está modernizada gracias a la implementación de CustomTkinter.
2. **Tablas Múltiples Dinámicas**: Independientemente de cuántas columnas devuelva Pandas, el `Treeview` de Tkinter incrustado las lee y se estructura dinámicamente sobre la marcha.
3. **El panel de 'Justificación'**: Por diseño, se añadió un panel exclusivo inferior en la pantalla principal. Cada consulta lleva anexa un bloque de texto validado que aclara "por qué" y el "propósito de negocio" de dicha consulta, tal como se ordenó.
4. **Gráficos Analíticos Integrados**: En consultas selectas (como _Duración Promedio_, _Series con más temporadas_), se habilitará un botón que procesa datos de `pandas` y los dibuja mediante `matplotlib` en ventanas flotantes estéticas.

## Cómo Ejecutarlo

Asegúrate de instalar los requerimientos previos desde tu consola principal:

```bash
pip install customtkinter pandas matplotlib
```

1. Ingresa a la carpeta del proyecto específico: `cd "2do Parcial\Proyecto_Netflix"`.
2. Ejecuta el comando `python main.py`.
3. Inicia sesión con cualquiera de los credenciales de `data/usuarios.txt`, por ejemplo: **admin** y contraseña **1234**.
4. Haz clic en las herramientas del panel izquierdo para ejecutar el análisis asociado de Netflix.
