![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Herramientas de los notebooks de resumen de Python

> Esta carpeta es para quien **mantiene** los notebooks, no para los estudiantes. El formato que se define aquí aplica **solo** a los notebooks de `laboratorios/resumen-python/`.

Los notebooks de esta carpeta no se editan a mano: cada uno se **genera** con un script de contenido, que garantiza que todos tengan el mismo formato y que sus salidas sean reales.

| Archivo | Para qué sirve |
|---|---|
| `formato.py` | Formato común: insignias, encabezado con objetivos, índice con anclas, "Cómo usar este notebook", marcas (🔮 ⚠️ 📏 🔎), enlaces a Python Tutor, salidas esperadas de las celdas con `input()`, ejercicios y ejecución. |
| `construir_<notebook>.py` | Contenido de un notebook: `construir_repaso_basico.py`, `construir_control_de_flujo.py`. |
| `verificar.py` | Comprueba que un notebook cumple el formato. |

## Requisitos

Python 3.11 con `nbformat`, `nbclient` e `ipykernel` (vienen con Anaconda / Jupyter).

## Uso

Desde la raíz del repositorio:

```
python laboratorios/resumen-python/herramientas/construir_repaso_basico.py
python laboratorios/resumen-python/herramientas/verificar.py laboratorios/resumen-python/estructurada_python/repaso_basico.ipynb --enlaces
```

Para cambiar un notebook, edite su `construir_<notebook>.py` (nunca el `.ipynb`) y vuelva a generarlo: así los enlaces a Python Tutor, el índice y las salidas quedan sincronizados con el código.

Después de generar, compare con `git diff`: es normal que aparezcan diferencias mínimas en las salidas (Jupyter a veces entrega una misma línea en dos trozos, o cambia el número del archivo interno en los `SyntaxError`). Si solo cambió eso, no hace falta hacer commit.

## Cómo crear un notebook nuevo

1. Copie `construir_repaso_basico.py` como `construir_<nombre>.py`.
2. Cambie el nombre del archivo, el título, la introducción y los objetivos en `nb.encabezado(...)`.
3. Escriba las secciones con `nb.md(...)`, `nb.code(...)` (con `entradas=[...]` si la celda usa `input()`), `nb.prediga(...)`, `nb.error(...)` y `nb.convencion(...)`.
4. Si hay contenido que no se ha visto en clase, póngalo en una sección final `## Para explorar: ...` con una explicación mínima.
5. Cierre con `nb.resumen_errores([...])` (cada error de la tabla debe tener una celda que lo muestre), `nb.ejercicios([...])` y "Recursos adicionales".
6. Genere el notebook y páselo por `verificar.py`.
