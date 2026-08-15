![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Clase 3 — Conceptos básicos de Python (Teoría)

Diapositivas base del tema 3: primer contacto en profundidad con Python, partiendo de los mismos tres ejemplos guiados de la clase 2 (área de triángulo, meses entre dos años, área de un círculo) pero ya codificados y ejecutados. Se centra en variables, cadenas de texto, entrada/salida por consola y buenas prácticas de comentarios. 40 diapositivas.

## Contenido cubierto

- **Repaso rápido**: método de Polya, diseño de algoritmos y pseudocódigo, como puente hacia Python.
- **Ciclo de desarrollo de un programa**: diseñar → escribir el código → corregir errores de sintaxis → probar → corregir errores de lógica.
- **Variables en Python**: equivalencia entre los tipos de pseudocódigo (`Entero`, `Real`, `Lógico`, `Texto`) y los tipos nativos de Python (`int`, `float`, `bool`, `str`); Python no distingue carácter de cadena.
- **Prueba de escritorio** aplicada a una secuencia de asignaciones aritméticas.
- **Cadenas de texto en Python**: creación (comillas simples/dobles/triples), concatenación (`+`) y repetición (`*`), caracteres de escape (`\n`, `\t`, `\"`, etc.), indexado (`cadena[posición]`, índices negativos) y *slicing* (`cadena[inicio:fin:paso]`).
- **Salida con `print()`**: sintaxis (`sep`, `end`), impresión de múltiples tipos, y formateo con f-strings (`f"..."`, incluyendo expresiones y formato numérico como `{promedio:.2f}`).
- **Entrada con `input()`**: siempre devuelve `str`; conversión explícita con `int()`/`float()` para poder operar.
- **Comentarios**: de una línea (`#`) y de varias líneas (`""" ... """`).
- **Tres ejemplos codificados y probados en Python**, con tabla de entradas/salidas esperadas: área de un triángulo, meses entre dos años, área de un círculo.
- **Ejercicios de repaso** para codificar en Python por cuenta propia (área/perímetro de un círculo, salario neto, edad en días, hipotenusa, operaciones básicas, corte de uñas).

## Recursos

| Archivo | Descripción |
|---|---|
| [clase-03.pdf](clase-03.pdf) | Diapositivas completas del tema 3, en PDF. |
| [clase-03.pptx](clase-03.pptx) | Diapositivas completas del tema 3, editable (PowerPoint). |
| [codigo_diapositivas/](codigo_diapositivas/) | Scripts de los tres ejemplos codificados en las diapositivas: `ejemplo1-area.py`, `ejemplo2-meses.py`, `ejemplo3-circulo.py`. |
| [codigo_diapositivas.zip](codigo_diapositivas.zip) | Los mismos scripts anteriores, empaquetados en un único zip. |
| [cadena_udea_index.png](cadena_udea_index.png) | Figura de apoyo: indexado carácter a carácter de la cadena `"Universidad de Antioquia"`. |

> [!Important]
> Se usó IA generativa para redactar y organizar este contenido a partir de las diapositivas de la clase. El docente revisó y validó la versión final.