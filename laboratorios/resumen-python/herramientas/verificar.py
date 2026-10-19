"""Comprueba que un notebook de laboratorios/resumen-python/ cumple el formato común.

Uso, desde la raíz del repositorio:
    python laboratorios/resumen-python/herramientas/verificar.py RUTA.ipynb [--enlaces]

Con --enlaces también comprueba que los enlaces externos respondan (tarda más).
No reemplaza la revisión visual en GitHub y Colab.
"""
import ast
import json
import re
import sys
import urllib.parse
import urllib.request

SECCIONES = ["## Objetivos", "## Índice", "## Cómo usar este notebook",
             "## Resumen: errores frecuentes", "## Ejercicios: prediga la salida",
             "## Recursos adicionales"]

ruta = sys.argv[1]
nb = json.load(open(ruta, encoding="utf-8"))
celdas = nb["cells"]
src = ["".join(c["source"]) for c in celdas]
todo = "\n".join(src)
problemas = []


def ok(cond, mensaje):
    if not cond:
        problemas.append(mensaje)


# 1. Insignias en la primera celda
ok("colab-badge.svg" in src[0] and "Built%20with-AI" in src[0], "La primera celda no tiene las dos insignias")
nombre = ruta.replace("\\", "/").split("/")[-1]
ok(src[0].count(nombre) >= 1, f"El enlace de Colab no apunta a {nombre}")

# 2. Secciones obligatorias
for s in SECCIONES:
    ok(any(re.search(rf"^{re.escape(s)}$", x, re.M) for x in src), f"Falta la sección '{s}'")
ok("📋 **Antes de empezar.**" in todo, "Falta el recuadro 'Antes de empezar'")

# 3. Anclas del índice
ids = set(re.findall(r'<a id="([^"]+)"', todo))
rotas = [l for l in re.findall(r"\]\(#([^)]+)\)", todo) if l not in ids]
ok(not rotas, f"Enlaces internos sin ancla: {rotas}")

# 4. Cada celda de código va seguida de su enlace a Python Tutor con el mismo código
codigo = [i for i, c in enumerate(celdas) if c["cell_type"] == "code"]
for i in codigo:
    sig = src[i + 1] if i + 1 < len(src) else ""
    m = re.search(r"pythontutor\.com/visualize\.html#code=([^&]+)", sig)
    ok(m and urllib.parse.unquote(m.group(1)) == src[i], f"Celda {i}: falta el enlace a Python Tutor o no coincide con el código")

# 5. Celdas con input(): sin salida y con la salida esperada debajo
def llama_input(fuente):
    try:
        arbol = ast.parse(fuente)
    except SyntaxError:
        return False
    return any(isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == "input"
               for n in ast.walk(arbol))


for i in codigo:
    usa_input = llama_input(src[i])
    sin_salida = not celdas[i]["outputs"]
    if usa_input:
        ok(sin_salida, f"Celda {i}: usa input() y tiene salida guardada")
        ok("Esta celda usa `input()`" in src[i + 1], f"Celda {i}: usa input() y no muestra la salida esperada")
    else:
        ok(not sin_salida or not src[i].strip(), f"Celda {i}: no tiene salida (¿se ejecutó el notebook?)")

# 6. Errores: listar las celdas que fallan, y que cada error de la tabla resumen tenga su ejemplo
errores = {}
for i in codigo:
    for o in celdas[i]["outputs"]:
        if o["output_type"] == "error":
            errores.setdefault(o["ename"], []).append(i)
tabla = next((x for x in src if x.lstrip().startswith(("<a id=\"resumen-errores-frecuentes\"", "## Resumen: errores frecuentes"))), "")
for nombre_error in sorted(set(re.findall(r"^\| `(\w+Error)`", tabla, re.M))):
    ok(nombre_error in errores, f"{nombre_error} está en la tabla resumen pero ninguna celda lo muestra")
avisos = []
for nombre_error, lista in errores.items():
    for i in lista:
        previa = src[i - 1] if i > 0 else ""
        if not ("⚠️" in previa or nombre_error in previa or "error" in src[i].lower()):
            avisos.append(f"Celda {i}: lanza {nombre_error}, pero ni la celda anterior ni un comentario lo anuncian")

# 7. Ejercicios: el enlace de cada solución tiene el mismo código del enunciado
ej = next((x for x in src if "**Ejercicio 1**" in x), "")
for code, u in re.findall(r"```python\n(.*?)\n```\n\n<details>.*?visualize\.html#code=([^&]+)", ej, re.S):
    ok(urllib.parse.unquote(u) == code, "Un ejercicio tiene un enlace a Python Tutor distinto de su código")

# 8. Enlaces externos (opcional)
if "--enlaces" in sys.argv:
    urls = sorted({u for u in re.findall(r"https?://[^\s)\]\"'>]+", todo)
                   if "pythontutor.com/visualize" not in u and "colab.research.google.com/github" not in u})
    for u in urls:
        try:
            req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
            codigo_http = urllib.request.urlopen(req, timeout=20).status
        except Exception as e:  # noqa: BLE001
            codigo_http = getattr(e, "code", type(e).__name__)
        if codigo_http != 200:
            avisos.append(f"Enlace {u} -> {codigo_http} (algunos sitios bloquean consultas automáticas: "
                          "ábralo en el navegador antes de quitarlo)")

print(f"{ruta}: {len(celdas)} celdas, {len(codigo)} de código")
print("Celdas que fallan:", {k: v for k, v in sorted(errores.items())})
for a in avisos:
    print("  aviso:", a)
if problemas:
    print(f"{len(problemas)} problema(s):")
    for p in problemas:
        print("  -", p)
    sys.exit(1)
print("Formato OK")
