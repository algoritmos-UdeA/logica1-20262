"""Formato común de los notebooks de laboratorios/resumen-python/.

Cada notebook se arma con un script de contenido (construir_<nombre>.py) que
usa esta clase. Aquí está todo lo que debe ser igual en todos los notebooks:
insignias, encabezado con objetivos, índice con anclas, "Cómo usar este
notebook", marcas, enlaces a Python Tutor, salidas esperadas de las celdas con
input(), ejercicios de "prediga la salida" y la ejecución con salidas reales.

Este formato es solo para los notebooks de esta carpeta.
"""
import contextlib
import copy
import io
import json
import re
import unicodedata
import urllib.parse

import nbformat
from nbclient import NotebookClient

REPO = "algoritmos-UdeA/logica1-20262"
CARPETA = "laboratorios/resumen-python/estructurada_python"

TUTOR = ("https://pythontutor.com/visualize.html#code={code}&cumulative=false"
         "&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js"
         "&py=311&rawInputLstJSON={inp}&textReferences=false")

PREDIGA = "> 🔮 **Prediga antes de ejecutar.** "
ERROR = "> ⚠️ **Error frecuente.** "
CONV = "> 📏 **Convención del curso.** "

ANTES_DE_EMPEZAR = ("Este notebook supone que usted ya sabe qué es un algoritmo y qué hace un "
                    "programa: recibe datos, los procesa y muestra resultados. No necesita tener "
                    "a mano el material de las clases; todo lo que se usa aquí se explica aquí.")

COMO_USAR = """
## Cómo usar este notebook

- Ejecute las celdas **en orden**, de arriba hacia abajo (`Shift + Enter`). Si algo se comporta raro, use *Reiniciar y ejecutar todo* (en Colab: **Entorno de ejecución → Reiniciar sesión y ejecutar todo**).
- Cambie los valores de los ejemplos y vuelva a ejecutar: es la mejor forma de comprobar si entendió.
- Algunas celdas **fallan a propósito** para mostrar un error; lea el mensaje, es parte del ejemplo.
- Para probar sus propias ideas, cree una celda de código nueva: en Colab, con el botón **+ Código** de la barra superior; en Jupyter, seleccione una celda (sin estar escribiendo en ella) y presione `B` para crear una debajo.

A lo largo del notebook encontrará estas marcas:

| Marca | Qué significa |
|---|---|
| 🔮 **Prediga antes de ejecutar** | Escriba en papel qué cree que imprime la celda y solo después ejecútela. |
| ⚠️ **Error frecuente** | Un error típico: el mensaje que da Python y cómo corregirlo. |
| 📏 **Convención del curso** | Una forma de escribir el código que se acordó en el curso. |
| 🔎 **Ver paso a paso en Python Tutor** | Abre esa misma celda en [Python Tutor](https://pythontutor.com/), donde puede avanzar instrucción por instrucción y ver cómo cambian las variables. Si la celda usa `input()`, el enlace ya trae los datos de ejemplo cargados. |

Además del índice de arriba, en Colab puede usar el panel **Índice** (el ícono ☰ de la izquierda) para saltar entre secciones.
"""

INTRO_EJERCICIOS = ("Para cada fragmento, escriba primero en papel lo que cree que imprime. Luego "
                    "despliegue la solución o abra el enlace de Python Tutor para comprobarlo paso "
                    "a paso. Si quiere ejecutarlos aquí, cree una celda de código nueva y copie el "
                    "fragmento.")


def tutor(fuente, entradas=None):
    """Enlace a Python Tutor con el código y, si hay input(), los datos de ejemplo."""
    return TUTOR.format(code=urllib.parse.quote(fuente, safe=""),
                        inp=urllib.parse.quote(json.dumps(entradas or [], ensure_ascii=False), safe=""))


def simular(fuente, entradas=()):
    """Ejecuta el código con input() simulado y devuelve la consola tal como se vería."""
    cola = list(entradas)
    buf = io.StringIO()

    def fake_input(msg=""):
        valor = cola.pop(0)
        buf.write(msg + valor + "\n")
        return valor

    with contextlib.redirect_stdout(buf):
        exec(fuente, {"input": fake_input})
    return buf.getvalue().rstrip("\n")


def slug(titulo):
    t = unicodedata.normalize("NFKD", titulo).encode("ascii", "ignore").decode()
    t = re.sub(r"[^\w\s-]", "", t.lower())
    return re.sub(r"[\s_]+", "-", t).strip("-")


class Notebook:
    """Acumula las celdas de un notebook y lo arma con el formato común."""

    def __init__(self, archivo):
        self.archivo = archivo          # p. ej. "repaso_basico.ipynb"
        self.celdas = []                # (tipo, fuente, entradas o None)

    # ------------------------------------------------------------ celdas
    def md(self, texto):
        self.celdas.append(("markdown", texto.strip("\n"), None))

    def code(self, fuente, entradas=None):
        """Celda de código. Si usa input(), pase en `entradas` los datos de ejemplo."""
        self.celdas.append(("code", fuente.strip("\n"), entradas))

    def prediga(self, texto):
        self.md(PREDIGA + texto)

    def error(self, texto):
        self.md(ERROR + texto)

    def convencion(self, texto):
        self.md(CONV + texto)

    # ------------------------------------------------------------ partes fijas
    def insignias(self):
        colab = f"https://colab.research.google.com/github/{REPO}/blob/main/{CARPETA}/{self.archivo}"
        self.md(f"[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]({colab}) "
                "[![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)](https://shields.io/)")

    def encabezado(self, titulo, intro, objetivos, antes_de_empezar=ANTES_DE_EMPEZAR):
        """Título, introducción, "Antes de empezar", objetivos, índice y "Cómo usar"."""
        lista = "\n".join(f"{k}. {o}" for k, o in enumerate(objetivos, 1))
        self.md(f"# {titulo}\n\n{intro}\n\n> 📋 **Antes de empezar.** {antes_de_empezar}\n\n"
                f"## Objetivos\n\nAl terminar este notebook, usted debería poder:\n\n{lista}")
        self.md("__INDICE__")
        self.md(COMO_USAR)

    def ejercicios(self, fragmentos):
        """Sección "Ejercicios: prediga la salida"; las soluciones se calculan ejecutando."""
        self.md(f"## Ejercicios: prediga la salida\n\n{INTRO_EJERCICIOS}")
        bloques = []
        for k, ej in enumerate(fragmentos, 1):
            ej = ej.strip("\n")
            bloques.append(f"""
**Ejercicio {k}**

```python
{ej}
```

<details>
<summary>Ver solución</summary>

```
{simular(ej)}
```

🔎 [Ver paso a paso en Python Tutor]({tutor(ej)})

</details>
""")
        self.md("\n".join(bloques))

    # ------------------------------------------------------------ armar
    def _indice(self):
        entradas, usados = [], set()
        for k, (tipo, fuente, entr) in enumerate(self.celdas):
            if tipo != "markdown" or fuente == "__INDICE__":
                continue
            nuevas = []
            for linea in fuente.split("\n"):
                m = re.match(r"^(##|###) (.+)$", linea)
                if m and m.group(2) != "Objetivos":
                    nivel, titulo = len(m.group(1)), m.group(2)
                    s = base = slug(titulo)
                    n = 2
                    while s in usados:
                        s, n = f"{base}-{n}", n + 1
                    usados.add(s)
                    nuevas.append(f'<a id="{s}"></a>\n')
                    entradas.append("  " * (nivel - 2) + f"- [{titulo}](#{s})")
                nuevas.append(linea)
            self.celdas[k] = (tipo, "\n".join(nuevas), entr)
        pos = [c[1] for c in self.celdas].index("__INDICE__")
        self.celdas[pos] = ("markdown", "## Índice\n\n" + "\n".join(entradas), None)

    def escribir(self, ruta):
        """Arma el notebook, lo ejecuta con Python (salidas reales) y lo guarda."""
        self._indice()
        nb = nbformat.v4.new_notebook()
        nb.metadata = {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
                       "language_info": {"name": "python"}}
        for tipo, fuente, entradas in self.celdas:
            if tipo == "markdown":
                nb.cells.append(nbformat.v4.new_markdown_cell(fuente))
                continue
            c = nbformat.v4.new_code_cell(fuente)
            nb.cells.append(c)
            texto = ""
            if entradas is not None:
                c.metadata["usa_input"] = True
                texto = ("Esta celda usa `input()`. Por ejemplo, si el usuario escribe "
                         + " y ".join(f"`{e}`" for e in entradas) + ", la salida es:\n\n```\n"
                         + simular(fuente, entradas) + "\n```\n\n")
            nb.cells.append(nbformat.v4.new_markdown_cell(
                texto + f"🔎 [Ver paso a paso en Python Tutor]({tutor(fuente, entradas)})"))

        # Las celdas con input() no se pueden ejecutar sin usuario: se reemplazan
        # temporalmente por `pass` y quedan sin salida guardada.
        ejec = copy.deepcopy(nb)
        for c in ejec.cells:
            if c.cell_type == "code" and c.metadata.get("usa_input"):
                c.source = "pass"
        NotebookClient(ejec, timeout=60, kernel_name="python3", allow_errors=True).execute()
        n = 0
        for c, e in zip(nb.cells, ejec.cells):
            if c.cell_type != "code":
                continue
            if c.metadata.pop("usa_input", None):
                c.outputs, c.execution_count = [], None
            else:
                n += 1
                c.outputs, c.execution_count = e.outputs, n
        nb.metadata["language_info"] = ejec.metadata["language_info"]
        for c in nb.cells:
            c.pop("id", None)
        nb.nbformat_minor = 4
        nbformat.write(nb, ruta)
        print(f"{ruta}: {len(nb.cells)} celdas")
