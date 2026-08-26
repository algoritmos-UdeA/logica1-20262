![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Clase 6 — Condicionales múltiples (Teoría)

Diapositivas base del tema 6: continuación directa de la clase 5, donde tras repasar alternativa simple y doble se introduce la **alternativa múltiple** — cuándo se necesita, cómo anidar bloques `Si...Entonces...Sino` (mismo criterio vs. criterios distintos) y su implementación en Python con `if` anidados o con `elif`. Se retoman los ejemplos del bar de Moe y el subsidio de transporte para corregirles bugs, y se desarrollan dos ejemplos nuevos de principio a fin: las notas de Springfield y una nómina semanal por horas. 69 diapositivas.

## Contenido cubierto

- **Repaso**: resumen del método de Polya, el modelo entrada-procesamiento-salida y la tabla de equivalencias (diagrama de bloques / pseudocódigo / Python), ya incorporando el bloque de decisión visto en la clase 5.
- **Casos en los problemas de decisión lógica**: alternativa simple, alternativa doble y alternativa múltiple.
- **Alternativa múltiple**: se necesita cuando hay más de dos alternativas; se implementa anidando bloques `Si...Entonces...Sino`. La forma de anidar depende del problema — **mismo criterio** (p. ej. rangos de una misma variable) se encadena, **criterios distintos** (p. ej. un umbral que cambia según la rama tomada) se anida condición completa dentro de condición.
- **`if`/`else` anidados en Python**: a diferencia del pseudocódigo, Python no tiene `Fin_Si`; es la **indentación** la que delimita dónde empieza y termina cada bloque, y a medida que crecen los anidamientos se vuelve más difícil de leer.
- **`if`/`elif`/`else`**: la palabra clave `elif` (contracción de `else if`) evita que la indentación crezca con cada nueva condición cuando todas evalúan el mismo criterio — cada alternativa queda al mismo nivel en vez de anidada dentro del `else` anterior.
- **Encadenamiento de operadores relacionales**: Python permite expresar un rango como `60 <= nota_num < 70`, de forma similar a como se escribiría matemáticamente, como alternativa a combinar dos comparaciones con `and`.
- **Ejemplo 1 (bar de Moe)**: retomado de la clase 5 para corregirle el bug — la versión original solo distinguía `'F'`/`'M'` en mayúscula y cobraba el precio de hombre a cualquier otro valor; se itera en 4 versiones hasta aceptar minúsculas y reportar un mensaje de error explícito para un género no reconocido en vez de asumir un valor por defecto.
- **Ejemplo 2 (subsidio de transporte)**: retomado para manejar el caso de un `sal_base` negativo (dato inválido) como una alternativa adicional, en vez de calcular un subsidio o salario neto sin sentido.
- **Ejemplo 3 (notas de Springfield)**: clasifica una nota numérica `[0,100]` en su letra equivalente (A-E), con validación de rango. Se resuelve de tres formas comparables — `if`/`else` anidados, `if`/`elif`/`else`, y una tercera con una seguidilla de `if` independientes usando rangos encadenados — con pruebas de escritorio y casos de test para verificar que todas producen el mismo resultado.
- **Ejemplo 4 (nómina semanal)**: calcula el salario neto de un trabajador a partir de las horas trabajadas (con recargo del 50% en las horas por encima de 35) y unos impuestos por tramos sobre el salario bruto (tres tramos: libre, 20%, 30%), con definición completa de variables, proceso paso a paso y prueba de escritorio sobre varios casos.
- **Ejercicios de repaso**: descuento por número de manzanas compradas, identificar la esfera de peso diferente entre cuatro, mostrar el mayor de tres números, determinar si un triángulo es rectángulo a partir de dos ángulos, incentivos salariales por categoría y unidades producidas, precio de un producto en la máquina dispensadora de Apu.
- 10 referencias externas: ellibrodepython, w3resource, Real Python (sitio general, cheatsheet y guías específicas de condicionales/buenas prácticas), curriculumresources.edu.gh, python-course.eu, y dos cursos de MakeCode Micro:bit (`csintro` y el listado general de cursos) — estos últimos no aparecían en las referencias de la clase 5.

## Recursos

| Archivo | Descripción |
|---|---|
| [clase-06.pdf](clase-06.pdf) | Diapositivas completas del tema 6, en PDF (69 páginas). |
| [clase-06.pptx](clase-06.pptx) | Diapositivas completas del tema 6, editable (PowerPoint). |
| [diagramas/](diagramas/) | Fuentes `.drawio` de los diagramas de flujo de cada versión de los ejemplos (bar de Moe, subsidio de transporte, notas de Springfield, nómina semanal). |
| [images/](images/) | Exportación en `.png` de la mayoría de los diagramas de `diagramas/`, con el mismo nombre de archivo (no todas las versiones intermedias tienen imagen exportada). |

### Código de ejemplo

| Código | Descripción |
|---|---|
| [codigo/ejemplo1_v0.py](codigo/ejemplo1_v0.py) | Bar de Moe, primera versión (con bug): solo compara `sex == 'F'` en mayúscula; cualquier otro valor, incluida `'f'` minúscula, cobra el precio de hombre. |
| [codigo/ejemplo1_v1.py](codigo/ejemplo1_v1.py) | Agrega `'f'` minúscula a la condición de mujer (`sex == 'F' or sex == 'f'`), pero sigue sin distinguir el resto de casos: todo lo demás cae en la rama de hombre. |
| [codigo/ejemplo1_v2.py](codigo/ejemplo1_v2.py) | Pasa a alternativa múltiple, anidando un `if` dentro del `else` para distinguir `'M'`/`'m'` explícitamente. |
| [codigo/ejemplo1_v3.py](codigo/ejemplo1_v3.py) | Versión final: agrega una tercera rama que informa `'Importe: Cobro normal'` cuando el sexo digitado no es ni hombre ni mujer, en vez de dejarlo sin manejar. |
| [codigo/ejemplo2_v0.py](codigo/ejemplo2_v0.py) | Subsidio de transporte, versión original: calcula el subsidio sin validar que `sal_base` sea un valor válido (puede ser negativo). |
| [codigo/ejemplo2_v1.py](codigo/ejemplo2_v1.py) | Agrega una alternativa múltiple con una bandera `flag_sal_valido` para detectar un `sal_base` fuera de rango y evitar calcular un salario neto sin sentido. |
| [codigo/ejemplo3_v1.py](codigo/ejemplo3_v1.py) | Notas de Springfield, forma 1: clasificación de la nota en letra con `if`/`else` anidados. |
| [codigo/ejemplo3_v2.py](codigo/ejemplo3_v2.py) | Notas de Springfield, forma 2: la misma clasificación reescrita con `if`/`elif`/`else`, reduciendo el anidamiento. |
| [codigo/ejemplo3_v3.py](codigo/ejemplo3_v3.py) | Notas de Springfield, forma 3: seguidilla de `if` independientes, cada uno con su rango acotado por comparaciones encadenadas (p. ej. `80 <= nota_num < 90`). |
| [codigo/ejemplo4.py](codigo/ejemplo4.py) | Nómina semanal completa: horas normales/extra, impuestos por tramos sobre el salario bruto, y una colilla de pago formateada como salida. |

> [!Important]
> Se usó IA generativa para redactar y organizar este contenido a partir de las diapositivas de la clase. El docente revisó y validó la versión final.
