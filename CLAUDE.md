# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository state

This is a course repository for "Lógica y Representación I" (UdeA, 2026-2). It currently contains no source code, build tooling, or tests — only course planning documents and reference material:

- `README.md` — full course overview (in Spanish): general info, purpose, learning outcomes, thematic units, summarized schedule, evaluation weights, methodology (flipped classroom + project-based learning), reference bibliography, complementary online courses/judges/gamified platforms, and communication channels
- `2508208_LÓGICA Y REPRESENTACIÓN I.pdf` — official course microcurriculum/syllabus
- `planeacion_tentativa/cronograma.md` — tentative semester schedule (superseded the old `planeacion/cronograma.md`, now removed): session-by-session topics (continuous class numbering 1–48 across 16 weeks), the fixed weekly time slots (Monday lab, mid-week 4h theory block), evaluation weights/dates, and notes on how the unit order and weekly slot order deviate from the official microcurriculum
- `clases/README.md` — index/table of contents of per-class materials (currently just a stub linking to each class folder)
- `clases/0/` — Clase 0 "Presentación del curso": `README.md` with instructor info, course logistics, and links to Google Classroom/repo, plus `clase_00.pdf` (slides) and `diagrama_clase0.drawio` (source diagram)
- `clases/1/` — Clase 1 "Conociendo las Herramientas de Trabajo": `README.md` covering required/optional tool installs (Anaconda, VS Code, draw.io, PyCharm), online practice tools (Python Tutor, CodeSkulptor), gamified warm-up activities (Code.org), and a student checklist
- `clases/<n>/README.md` files are marked as drafted with generative AI from instructor prompts and reviewed by the instructor
- `material/cheat-sheets/` — quick-reference PDFs for Python and Java-vs-Python comparisons (e.g. `beginners_python_cheat_sheet_pcc_all.pdf`, `mementopython3-english.pdf`, `Java4Python.pdf`, `java_vs_python.pdf`, the Coding Club Python series, `CC-CodeCards.pdf`)
- `material/libros/` — full reference textbooks (PDF) on programming logic and Python: `Joyce-Farrell_Programming-Logic-and-Design.pdf`, `Joyce-Farrell_Introduccion-a-la-programacion.pdf` (renamed from their original accented/special-character filenames), `Florez-Rueda-Roberto_2011_Algoritmia-Basica.pdf`, `Logica-de-Programacion-Efrain-Oviedo.pdf`, `Python Crash Course_...pdf`, `Introduction-to-programming-using-Python-3.pdf`

There is nothing to build, lint, or test at this stage. When code is added to this repository, update this file with the actual commands and architecture rather than assuming a structure in advance.
