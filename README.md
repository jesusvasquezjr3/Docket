# 📋 Docket - Gestor de Tareas

<img src="images/logo.png" alt="Logo" width="150" align="right" style="margin-left: 20px; margin-bottom: 20px;" />

[![Hybridge Education](https://img.shields.io/badge/Hybridge-Education-lightgrey)](https://www.hybridge.education)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JSON](https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white)
![Markdown](https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white)


## Resumen
Docket es una aplicación de gestión de tareas sencilla y visualmente atractiva, desarrollada con **Python** y **Tkinter** . Permite a los usuarios añadir, eliminar y marcar tareas como completadas o incompletas, con una interfaz inspirada en el diseño de *glass morphism* que es limpia y responsiva, desarrollado para la clase de **Programación Avanzada** en la carrera de **Ingeniería en Inteligencia Artificial** en **Hybridge Education.**.

![Docket](images/Screenshot_2025-07-10_225000.png)

## ✨ Características
- ➕ **Añadir Tareas**: Introduce una tarea en el campo de entrada y haz clic en "Añadir" para incluirla en la lista.
- 🗑️ **Eliminar Tareas**: Selecciona una tarea y haz clic en "Eliminar" para quitarla.
- 🔄 **Cambiar Estado de Tarea**: Selecciona una tarea y haz clic en "Cambiar" para marcarla como completada (✅) o incompleta (⏳).
- 💾 **Almacenamiento Persistente**: Las tareas se guardan en un archivo `tasks.json` y persisten entre sesiones.
- 📏 **Diseño Responsivo**: La interfaz se adapta a diferentes tamaños de ventana.
- 🖼️ **Interfaz de *Glass Morphism***: Diseño moderno con un panel semitransparente, colores alternados en las filas y emojis de estado centrados.
- 🎨 **Mejoras Visuales**: Filas más anchas (30px de altura) con colores alternados (`#D5E8FF` para pares, `#EBF5FF` para impares) y texto negro para mejor legibilidad.
- 🖌️ **Iconos Personalizados**: Incluye un ícono y un logo de la aplicación (PNG, relación de aspecto 1:1).

## 🛠️ Requisitos
- 🐍 Python 3.6 o superior (Tkinter está incluido en la biblioteca estándar).
- 🔤 Una fuente del sistema que soporte emojis Unicode (por ejemplo, Segoe UI Emoji) para renderizar correctamente ✅ y ⏳.

## 🚀 Instalación
1. 📥 Clona el repositorio:
   ```bash
   git clone https://github.com/jesusvasquezjr3/Docket
   cd Docket
   ```
2. ✅ Asegúrate de tener Python instalado. Verifica con:
   ```bash
   python --version
   ```
3. 🖼️ Coloca los recursos de imagen requeridos en el directorio del proyecto:
   - `icon.png`: Ícono de la aplicación, PNG, relación de aspecto 1:1, símbolo simple de tarea.
   - `logo.png`: Logo de la aplicación, PNG, sin fondo, relación de aspecto 1:1.
   > ℹ️ **Nota**: Estas imágenes se referencian en `config.py`. Puedes usar imágenes de marcador de posición o crear las tuyas con relación de aspecto 1:1.
4. ▶️ Ejecuta la aplicación:
   ```bash
   python main.py
   ```

## 📂 Estructura del Proyecto
```plaintext
Docket/
├── 📄 main.py              # Punto de entrada de la aplicación
├── 📄 task_manager.py      # Lógica de gestión de tareas
├── 📄 gui.py               # Interfaz gráfica de usuario
├── 📄 config.py            # Configuraciones y paleta de colores
├── 📄 utils.py             # Funciones de utilidad
├── 📄 tasks.json           # Almacenamiento de tareas (generado)
├── 🖼️ icon.png            # Ícono de la aplicación (PNG, 1:1)
└── 🖼️ logo.png            # Logo de la aplicación (PNG, 1:1)
```

- `main.py`: Inicializa la aplicación y conecta los componentes 🚀.
- `task_manager.py`: Gestiona la lógica de las tareas (añadir, eliminar, cambiar estado) y la persistencia en `tasks.json` 💾.
- `gui.py`: Define la interfaz gráfica, incluyendo el `Treeview` para las tareas, el campo de entrada y los botones 🖥️.
- `config.py`: Almacena constantes como colores y rutas de recursos 🎨.
- `utils.py`: Placeholder para funciones de utilidad (por ejemplo, simulación de fondo degradado) 🛠️.
- `tasks.json`: Archivo generado automáticamente para almacenar las tareas de forma persistente 📋.
- `icon.png` y `logo.png`: Recursos de imagen para el ícono y el logo de la aplicación 🖼️.

## 📖 Uso
1. ▶️ Inicia la aplicación ejecutando `python main.py`.
2. ➕ **Añadir una Tarea**: Escribe una tarea en el campo de entrada y haz clic en "Añadir".
3. 🗑️ **Eliminar una Tarea**: Selecciona una tarea en la lista y haz clic en "Eliminar".
4. 🔄 **Cambiar Estado de Tarea**: Selecciona una tarea y haz clic en "Cambiar" para alternar entre completada (✅) e incompleta (⏳).
5. 💾 Las tareas se guardan automáticamente en `tasks.json` y se cargan al iniciar la aplicación.
6. 🎨 La interfaz incluye:
   - 📋 Un `Treeview` con columnas de tareas y estado, con emojis centrados.
   - 🌈 Colores alternados en las filas para separación visual.
   - 📏 Filas más anchas (30px de altura) con texto negro para mejor legibilidad.
   - 🖼️ Un diseño inspirado en *glass morphism* con un panel semitransparente y una paleta de colores con tonos azules, naranjas y morados.

## 📜 Licencia MIT
Copyright © 2025 Jesús Vásquez - Hybridge Education

Este proyecto es material académico desarrollado como parte del programa educativo de Hybridge Education.

## 📜 Licencia
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

*Desarrollado con Python y Tkinter por [Tu Nombre] 🧑‍💻.*
