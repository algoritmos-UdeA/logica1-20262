![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Clase 7 — Ciclos

Continuación de la clase 6: tras cerrar el bloque de condicionales, se introduce la estructura repetitiva o **ciclo** (`Mientras`/`while`) — motivada por el problema de imprimir cada vez más números en pantalla — junto con sus componentes (inicialización, condición de control, cuerpo, actualización) y los tipos de variables de apoyo (contador, acumulador, bandera, centinela), desarrollados en siete ejemplos guiados.

## Teoría

- [`teoria/README.md`](teoria/README.md) — resumen del tema completo: repaso de año bisiesto como puente, la estructura `Mientras`/`while`, tipos de variables en ciclos (contador, acumulador, bandera, centinela), y los ejemplos guiados (imprimir N números, suma de números, factorial, secuencia alternante de signos, el cine del señor Burns, y las notas de un curso con iteraciones desconocidas/conocidas).
- [`teoria/clase-07.pdf`](teoria/clase-07.pdf) / [`teoria/clase-07.pptx`](teoria/clase-07.pptx) — diapositivas completas (91 diapositivas).

## Sesiones magistrales

| Sesión | Fecha | Modalidad | Contenido cubierto | Detalle |
|---|---|---|---|---|
| 12 | Mar 1 sep (bloque 2, 16-18) | 🏫 Presencial | Primer contacto práctico con ciclos: `hola_ciclos` (contar iteraciones de un `while`) y dos formas de generar la serie de números pares hasta `N` — filtrando pares con módulo desde un contador que avanza de 1 en 1, y generando directamente con paso 2 | [sesion_magistral-12](sesion_magistral-12/README.md) |
| 13 | Mar 8 sep (bloque 1, 14-16) | 🏫 Presencial | Componentes de un ciclo formalizados con 6 casos de repaso sobre la frontera de la condición, el orden de instrucciones y el ciclo infinito; luego contador y acumulador con un programa que clasifica pares e impares (cantidad y promedio de cada uno), depurado en vivo tras descubrir con una prueba de escritorio un bug de división por cero, corregido primero con `if` anidados y luego con `if-elif-else` | [sesion_magistral-13](sesion_magistral-13/README.md) |
| 14 | Mar 8 sep (bloque 2, 16-18) | 🏫 Presencial | **Parcial 1** — sin contenido nuevo de teoría | [sesion_magistral-14](sesion_magistral-14/README.md) |
| 15 | Mar 15 sep (bloque 1, 14-16) | 🏫 Presencial | Repaso del ejercicio de pares/impares de la sesión 13: comparación del reporte final con `if` anidados vs. `elif`, y tres formas de controlar el ciclo de lectura para el mismo enunciado — contador, bandera y centinela | [sesion_magistral-15](sesion_magistral-15/README.md) |
| 16 | Mar 15 sep (bloque 2, 16-18) | 🏫 Presencial | Orden de las instrucciones dentro del cuerpo de un ciclo (el mismo mecanismo del off-by-one); cuatro formas de ciclo infinito en Python (`while True`/`1`/`5`, y una variable de control sin actualizar); y ruptura de ciclos retomando el Ejemplo 8 de la teoría, agregando el caso sin ruptura para evidenciar el problema que la bandera y `break` resuelven | [sesion_magistral-16](sesion_magistral-16/README.md) |

> [!Important]
> Se usó IA generativa para redactar y organizar este contenido a partir del material de la clase. El docente revisó y validó la versión final.
