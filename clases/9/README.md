![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Clase 9 — Funciones: introducción

Tras un repaso de todo lo visto hasta ahora (condicionales, ciclos `Mientras` y `Para`, y tipos de variables de los ciclos), se introduce la idea de **modularizar**: dividir un programa en partes más pequeñas, llamadas **funciones**, cada una encargada de una sola tarea. Se explican las ventajas de hacerlo (abstracción, trabajo simultáneo, reutilización y confiabilidad), cómo nombrar las funciones, la relación entre función llamadora y función llamada, y la cohesión funcional. También se ve cómo definir e invocar funciones en Python, los cuatro tipos de funciones según sus entradas y salidas, y cómo probarlas con `assert` antes de integrarlas al programa. El tema se aplica a tres ejemplos: la conversión de temperatura y las calificaciones de un curso (el Ejemplo 5 de la [clase 8](../8/README.md)), resueltos sin funciones y con funciones, y un programa de áreas de figuras con menú, desarrollado paso a paso.

## Teoría

- [`teoria/README.md`](teoria/README.md) — resumen del tema completo: repaso, módulos y modularización, ventajas de modularizar, programa principal, cómo nombrar funciones, definición e invocación de funciones en Python, tipos de funciones, pruebas con `assert`, función llamadora y llamada, cohesión funcional, y los tres ejemplos.
- [`teoria/clase-09.pdf`](teoria/clase-09.pdf) / [`teoria/clase-09.pptx`](teoria/clase-09.pptx) — diapositivas completas (62 diapositivas).
- [`teoria/codigo/`](teoria/codigo/) — los scripts de los ejemplos: temperatura y calificaciones (cada uno sin funciones y con funciones), las siete formas de invocar una función, y el programa de áreas, en un solo archivo (`areas.py`) y dividido en tres (`areas_app/`).
- [`teoria/notebooks/funciones.ipynb`](teoria/notebooks/funciones.ipynb) — notebook guiado para convertir en funciones reutilizables cinco ejercicios de la clase 8 (el primero resuelto como modelo, los demás por completar, con pruebas `assert` ya escritas).

## Sesiones magistrales

| Sesión | Fecha | Modalidad | Contenido cubierto | Detalle |
|---|---|---|---|---|
| 23 | Mar 6 oct (bloque 2, 16-18) | 🏫 Presencial | Definición e invocación de funciones, comparando cada ejemplo sin función y con función para mostrar por qué se reutiliza: conversión de temperatura (`c_to_f`, `c_to_k` y un menú que las integra) y los ciclos anidados de la sesión 22 convertidos en funciones que imprimen (rectángulo de caritas, serie, triángulo y escalera de Mario), en un notebook. El programa de temperaturas hecho en clase es el punto de partida de la clase 10 | [sesion_magistral-23](sesion_magistral-23/README.md) |

La clase 9 empezó en el segundo bloque del 6 de octubre, después de terminar los ciclos anidados de la [clase 8](../8/sesion_magistral-22/README.md) en el primero.

> [!Important]
> Se usó IA generativa para redactar y organizar este contenido a partir del material de la clase. El docente revisó y validó la versión final.
