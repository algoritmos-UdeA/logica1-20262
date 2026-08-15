# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository state

This is a course repository for "Lógica y Representación I" (UdeA, 2026-2). It has no build tooling or test suite — it's course planning documents, reference material, and small standalone example scripts:

- `README.md` — full course overview (in Spanish): general info, purpose, learning outcomes, thematic units, summarized schedule, evaluation weights, methodology (flipped classroom + project-based learning), reference bibliography, complementary online courses/judges/gamified platforms, and communication channels
- `2508208_LÓGICA Y REPRESENTACIÓN I.pdf` — official course microcurriculum/syllabus
- `planeacion_tentativa/cronograma.md` — tentative semester schedule (superseded the old `planeacion/cronograma.md`, now removed): session-by-session topics (continuous class numbering 1–48 across 16 weeks), the fixed weekly time slots (Monday lab, mid-week 4h theory block), evaluation weights/dates, and notes on how the unit order and weekly slot order deviate from the official microcurriculum
- `clases/README.md` — index/table of contents of per-class materials, but it only links to clases 0-1 and is out of date; do not rely on it to know which class folders exist — check `clases/` directly
- `clases/0/` — Clase 0 "Presentación del curso": `README.md` with instructor info, course logistics, and links to Google Classroom/repo, plus `clase_00.pdf` (slides) and `diagrama_clase0.drawio` (source diagram)
- `clases/1/` — Clase 1 "Conociendo las Herramientas de Trabajo": `README.md` covering required/optional tool installs (Anaconda, VS Code, draw.io, PyCharm), online practice tools (Python Tutor, CodeSkulptor), gamified warm-up activities (Code.org), and a student checklist
- `clases/2/` — Clase 2, método de Polya / lógica de resolución de problemas: `clase-02.pdf`/`.pptx`, `template_polya/` (plantilla en blanco del método Polya + `README.md`), `apuntes_zoom/` (PDF anotado de la sesión, ejemplos `ejemplo_meses.py`/`ejemplo3_areacirculo.py`, y `resumen.md`), and `apuntes_zoom_2/` (notas de una segunda sesión de zoom: `apuntes_clase5*.xopp`/`.pdf`, `diagrama.drawio`/`.png`, `metodo_polya_nomina*`, `nomina.py`, `ejemplo_clase/`) — note that "clase5" in those filenames refers to the continuous session numbering in `cronograma.md`, not a `clases/5/` folder
- `clases/3/` — `clase-03.pdf`/`.pptx`, `codigo_diapositivas/` (code examples from the slides: `ejemplo1-area.py`, `ejemplo2-meses.py`, `ejemplo3-circulo.py`, also zipped as `codigo_diapositivas.zip`), and `ejemplos_clase/` (own `README.md`; `algoritmos/diagrama_nomina.drawio`/`.png`, `codigos/Circulo.py`)
- `clases/4/` — only `clase-04.pptx` so far, no `README.md` or PDF yet
- `clases/<n>/README.md` files are marked as drafted with generative AI from instructor prompts and reviewed by the instructor
- `material/cheat-sheets/` — quick-reference PDFs for Python and Java-vs-Python comparisons (e.g. `beginners_python_cheat_sheet_pcc_all.pdf`, `mementopython3-english.pdf`, `Java4Python.pdf`, `java_vs_python.pdf`, the Coding Club Python series, `CC-CodeCards.pdf`)
- `material/libros/` — full reference textbooks (PDF) on programming logic and Python: `Joyce-Farrell_Programming-Logic-and-Design.pdf`, `Joyce-Farrell_Introduccion-a-la-programacion.pdf` (renamed from their original accented/special-character filenames), `Florez-Rueda-Roberto_2011_Algoritmia-Basica.pdf`, `Logica-de-Programacion-Efrain-Oviedo.pdf`, `Python Crash Course_...pdf`, `Introduction-to-programming-using-Python-3.pdf`

The `.py` files under `clases/2/` and `clases/3/` are standalone didactic examples (stdlib only, no dependencies, no tests) — run them with `python <archivo>.py`. There is nothing to build, lint, or test at this stage. When more code is added to this repository, update this file with the actual commands and architecture rather than assuming a structure in advance.
