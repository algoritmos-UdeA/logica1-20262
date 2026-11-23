![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Cronograma real — Lógica y Representación I (2026-2)

Este cronograma muestra lo que **realmente se dictó**, semana por semana, para contrastarlo con el [cronograma tentativo](cronograma.md) que se planeó al inicio del semestre. Se construyó a partir del [índice de clases](../clases/README.md) y de las guías de los [laboratorios](../laboratorios/README.md). Está actualizado al **22 de noviembre de 2026**.

**Cómo leerlo:**

- La semana 1 empieza el lunes 3 de agosto de 2026.
- La columna **Sesiones** usa el número de sesión magistral del índice de clases (`sesion_magistral-N`), no la numeración 1-48 del cronograma tentativo.
- La columna **Clase** es la carpeta del tema en `clases/<n>/`.
- Los laboratorios de los lunes no tienen una carpeta por sesión. Solo aparecen las fechas de asignación y entrega que dicen sus guías.

## Semana por semana

| Semana | Fechas | Sesiones | Clase | Tema | Evaluaciones y laboratorios |
|---|---|---|---|---|---|
| 1 | 3-7 ago | 1-3 | 0, 1, 2 | Presentación del curso; conceptos básicos; algoritmos y diagramas de flujo (hasta las variables) | — |
| 2 | 10-14 ago | 4-6 | 2 | Método de Polya y planteamiento de algoritmos (ejemplo de la nómina). Las tres sesiones fueron virtuales | — |
| 3 | 17-21 ago | 7-8 | 3, 4 | Conceptos básicos de Python; operadores y expresiones. El lunes 17 fue festivo | Laboratorio 1 |
| 4 | 24-28 ago | 9-10 | 5, 6 | Condicionales simples y dobles; condicionales múltiples | — |
| 5 | 31 ago-4 sep | 11-12 | 6, 7 | Repaso de condicionales múltiples (nómina semanal); primer contacto con ciclos | — |
| 6 | 7-11 sep | 13-14 | 7 | Componentes de un ciclo; contador y acumulador | **Parcial 1** (sesión 14, 8 sep). Laboratorio 2: asignación el 5 sep |
| 7 | 14-18 sep | 15-16 | 7 | Bandera y centinela; ciclos infinitos y ruptura con `break` | Laboratorio 2: entrega el 19 sep |
| 8 | 21-25 sep | 17-18 | 8 | Ciclo `Para` (`for`): ejemplos 1 a 5 de la teoría | — |
| 9 | 28 sep-2 oct | 19-20 | 8 | Series; divisores y primos; notebooks en Jupyter y Colab; Fibonacci; máximo y mínimo | Laboratorio 3: asignación el 28 sep |
| 10 | 5-9 oct | 22-23 | 8, 9 | Ciclos anidados; funciones: definición e invocación | — |
| 11 | 12-16 oct | 24-25 | 10 | Pruebas con `assert` y especificación; ámbito y paso de argumentos. El lunes 12 fue festivo | Laboratorio 3: entrega el martes 13 oct |
| 12 | 19-23 oct | 26-27 | 10 | De un archivo a varios: *stubs*, módulos y la variable `__name__`; librerías (`math`, `random`) y diseño top-down | — |
| 13 | 26-30 oct | 28-29 | 11 | Arreglos unidimensionales: la lista usada como arreglo | **Parcial 2** (sesión 29, 27 oct) |
| 14 | 2-6 nov | 30-31 | 11, 12 | Funciones con listas; ordenamiento y búsqueda (el tema completo). El lunes 2 fue festivo | — |
| 15 | 9-13 nov | 32 | 13 | Programación orientada a objetos, bloque 1 (los dos bloques del día) | — |
| 16 | 16-20 nov | — | — | Sin sesión registrada en el índice de clases. El lunes 16 fue festivo | — |

La sesión 21 (clase 8) se preparó para el 6 de octubre, pero en clase se trabajaron otros ejemplos de ciclos anidados. Ese día quedó registrado como las sesiones 22 y 23.

## Lo que falta

Estas actividades están en orden, pero todavía no tienen fecha.

| Orden | Actividad | Material | Fecha |
|---|---|---|---|
| 1 | Clase 14 — Arreglos bidimensionales (matrices) | [Preparada](../clases/14/README.md): diapositivas, código y notebooks | Por definir |
| 2 | Clase 15 — Archivos | [Preparada](../clases/15/README.md): diapositivas, código y notebooks | Por definir |
| — | Parcial 3 — Programación orientada a objetos (15 %) | — | Por definir |
| — | Parcial 4 (20 %) | — | Por definir |
| — | Laboratorio 4 — Funciones | [Borrador](../laboratorios/4/README.md) | Por definir |
| — | Laboratorio 5 — POO: un parqueadero | [Borrador](../laboratorios/5/README.md) | Por definir |
| — | Proyecto de aula: entrega 2 y sustentación (20 %) | — | Por definir |

## Comparación con el cronograma tentativo

### Orden y duración de las unidades

| Unidad | Clases | Semanas planeadas | Semanas reales |
|---|---|---|---|
| Algoritmos secuenciales | 0-4 | 1-3 | 1-3 |
| Estructuras de control selectivas | 5-6 | 3-5 | 4-5 |
| Estructuras de control repetitivas | 7-8 | 5-8 | 5-10 |
| Funciones | 9-10 | No estaba como unidad | 10-12 |
| Arreglos unidimensionales | 11 | 10-11 | 13-14 |
| Ordenamiento y búsqueda | 12 | 10-11 (dentro de arreglos) | 14 |
| Programación orientada a objetos | 13 | 8-10 | 15 |
| Arreglos bidimensionales (matrices) | 14 | 11-12 | Por definir |
| Archivos | 15 | 13 | Por definir |

Orden planeado: secuenciales → selectivas → repetitivas → POO → arreglos 1D → arreglos 2D → archivos.

Orden real: secuenciales → selectivas → repetitivas → **funciones** → arreglos 1D → ordenamiento y búsqueda → **POO** → arreglos 2D → archivos.

### Evaluaciones

| Evaluación | Peso | Semana planeada | Semana real |
|---|---|---|---|
| Parcial 1 — Algoritmos secuenciales | 10 % | 3 | 6 (8 sep) |
| Parcial 2 — Estructuras de control | 20 % | 7 | 13 (27 oct) |
| Parcial 3 — Programación orientada a objetos | 15 % | 9 | Por definir |
| Parcial 4 — Arreglos (y archivos, según el cronograma tentativo) | 20 % | 14 | Por definir |
| Proyecto de aula, entrega 2 | 20 % | 16 | Por definir |

### Diferencias principales

- **Funciones se volvió una unidad propia.** El cronograma tentativo no la tenía, y ocupó cinco sesiones (de la 23 a la 27). Sirvió de base para todo lo que siguió: pruebas con `assert`, módulos y la organización en tres archivos que usan los laboratorios 4 y 5.
- **POO se movió después de arreglos.** Así, la clase 13 resuelve con objetos el mismo problema que la clase 12 resolvió con arreglos paralelos, y el arreglo de objetos ya no es un tema nuevo.
- **Ciclos tomó más tiempo del planeado.** Ocupó las semanas 5 a 10 en lugar de 5 a 8, con repasos de ciclos anidados.
- **Los parciales se corrieron.** El parcial 1 se hizo en la semana 6 y el parcial 2 en la semana 13.
- **Varios lunes fueron festivos**: 17 de agosto, 12 de octubre, 2 de noviembre y 16 de noviembre. La semana 2 fue virtual.
- **La semana 15 terminó en la clase 13.** El cronograma tentativo terminaba los contenidos en la semana 13, y en la semana 15 ya estaba la recta final del proyecto. Quedan por dictar las clases 14 y 15, además de los parciales 3 y 4.

> [!Important]
> Se usó IA generativa para construir este cronograma a partir del índice de clases y de las guías de laboratorio del repositorio. El docente revisa y valida la versión final.
