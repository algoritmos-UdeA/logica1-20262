![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Clase 10 — Funciones: diseño, librerías y módulos

Continuación de la [clase 9](../9/README.md). A partir del programa de conversión de temperaturas hecho en clase, se aplican **buenas prácticas** (nombres claros, pruebas con `assert`) y se introduce la **especificación** de una función (*Supone / Garantiza*), entendida como un contrato entre quien la escribe y quien la usa. También se estudian el **ámbito** de las variables (locales y globales), las formas de pasar argumentos, los **parámetros con valor por defecto** y las funciones que llaman a otras funciones. Para resolver problemas grandes se presenta el **diseño top-down**, que divide el problema en subproblemas y construye el programa paso a paso con *stubs*. Luego se usan **librerías**: las funciones integradas y los módulos `math` y `random`. Por último, el programa se organiza en **varios archivos** (módulos propios, `__name__`, `def main()` y la guarda `if __name__ == "__main__":`), la estructura que se usa en todos los programas del curso de aquí en adelante. La clase cierra con un problema que no se puede resolver bien sin **arreglos**, el tema siguiente.

## Teoría

- [`teoria/README.md`](teoria/README.md) — resumen del tema completo: buenas prácticas, especificación, ámbito de las variables, paso de argumentos y parámetros por defecto, funciones que llaman a otras, diseño top-down con stubs, funciones integradas y librerías (`math`, `random`), módulos propios y el problema que motiva los arreglos.
- [`teoria/clase-10.pdf`](teoria/clase-10.pdf) / [`teoria/clase-10.pptx`](teoria/clase-10.pptx) — diapositivas completas (60 diapositivas).
- [`teoria/codigo/README.md`](teoria/codigo/README.md) — **índice del código**: el enunciado de cada problema y los enlaces a los archivos que lo resuelven.
- [`teoria/codigo/`](teoria/codigo/) — los scripts de los ejemplos: el programa de temperaturas en sus versiones sucesivas (`v1` a `v3` y los pasos top-down), la función `seno` y su comparación con `math.sin`, el mismo programa dividido en módulos (`temperaturas_modulos/`) y el problema de las notas sin arreglos.
- [`teoria/codigo/adivina_numero/`](teoria/codigo/adivina_numero/) — ejercicio guiado de repaso que integra todo el tema, desde el diseño top-down hasta la división en módulos. Su sección 7 (opción 2: archivo de pruebas aparte) es el modelo de organización en archivos del [laboratorio 4](../../laboratorios/4/).

## Sesiones magistrales

| Sesión | Fecha | Modalidad | Contenido cubierto | Detalle |
|---|---|---|---|---|
| 24 | Mar 13 oct (bloque 1, 14-16) | 🏫 Presencial | El programa de temperaturas de la sesión 23 mejorado paso a paso: pruebas con `assert` en vez de `print`, funciones y pruebas separadas de la interacción con el usuario, nombres claros, especificación como contrato (*Supone / Garantiza*) y validación del dato con una constante y `continue` antes de llamar a la función | [sesion_magistral-24](sesion_magistral-24/README.md) |
| 25 | Mar 13 oct (bloque 2, 16-18) — tentativa | 🏫 Presencial | Pendiente por dictar | — |

La primera versión del programa de temperaturas (`teoria/codigo/temperaturas_v1.py`) se escribió en clase, en la sesión 23 de la [clase 9](../9/README.md). La sesión 24 retoma ese programa y lo mejora paso a paso, como camino hacia la división en varios archivos. Cuando se documente la sesión 25, se creará la carpeta `sesion_magistral-25/` y su fila se completará con su contenido y su enlace.

> [!Important]
> Se usó IA generativa para redactar y organizar este contenido a partir del material de la clase. El docente revisó y validó la versión final.
