![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Clases del curso

Índice de materiales por sesión magistral. Cada clase numérica agrupa su material en `teoria/` (diapositivas del tema completo, con un README que resume su contenido) y una carpeta `sesion_magistral-N/` por cada sesión que dictó ese tema — la numeración de sesión es continua a lo largo de todo el curso, no reinicia por clase.

**Leyenda de modalidad:** 🏫 Presencial · 💻 Virtual

## Tabla fusionada de sesiones (índice + bitácora)

Una fila por **sesión magistral real**, con el tema y el material vigentes a la fecha.

| Sesión | Fecha | Modalidad | Clase | Tema | Contenido cubierto | Sesión magistral |
|---|---|---|---|---|---|---|
| 1 | Lun 3 ago | 🏫 | [0](0/README.md) | Presentación del curso | Presentación del curso, completa | [sesion-magistral_1](0/sesion-magistral_1/README.md) |
| 2 | Mar 4 ago (bloque 1, 14-16) | 🏫 | [1](1/README.md) | Conceptos básicos (computador, hardware/software, lenguajes de programación) | Teoría del tema 1 completa | [sesion_magistral-2](1/sesion_magistral-2/README.md) |
| 3 | Mar 4 ago (bloque 2, 16-18) | 🏫 | [2](2/teoria/README.md) | Algoritmos y diagramas de flujo (método de Polya) | Teoría del tema 2 hasta la diapositiva 26 (variables), antes del método de Polya | [sesion_magistral-3](2/sesion_magistral-3/README.md) |
| 4 | Lun 10 ago | 💻 | [2](2/teoria/README.md) | Algoritmos y diagramas de flujo (método de Polya) | Continuación desde la diapositiva 26: método de Polya aplicado al planteamiento de algoritmos | [sesion_magistral-4](2/sesion_magistral-4/README.md) |
| 5 | Jue 13 ago | 💻 | [2](2/teoria/README.md) | Algoritmos y diagramas de flujo (método de Polya) | Refuerzo del planteamiento de algoritmos con el ejemplo de nómina | [sesion_magistral-5](2/sesion_magistral-5/README.md) |
| 6 | Vie 14 ago | 💻 | [2](2/teoria/README.md) | Algoritmos y diagramas de flujo (método de Polya) | Sesión breve: recuento rápido del material visto hasta el momento, para estudio propio; el contenido planeado se movió a la sesión 7 | [sesion_magistral-6](2/sesion_magistral-6/README.md) |
| 7 | Por confirmar | — | [3](3/teoria/README.md) | Conceptos básicos de Python | Pendiente por dictar | [sesion_magistral-7](3/sesion_magistral-7/README.md) *(README aún sin diligenciar)* |
| 8 | Mar 18 ago (bloque 2, 16-18) | 🏫 | [4](4/teoria/README.md) | Operadores y expresiones en Python | Pendiente por dictar | [sesion_magistral-8](4/sesion_magistral-8/README.md) |

> **Nota:** la sesión 8 quedó agendada para el martes 18 de agosto porque el 17 de agosto es festivo. La sesión 7 (clase 3) todavía no tiene fecha asignada en su README — vale la pena confirmar si va antes o después del 18 de agosto.

Notas sobre la fusión:
- La columna **Clase** enlaza al README del tema (o al PDF/teoría si aún no hay README), como en la tabla de índice actual.
- La columna **Estado** de la tabla de índice (`✅ Completo` / `🚧 Sin README`) se puede seguir mostrando, pero a nivel de *tema* (Clase), no de sesión — porque un tema abarca varias sesiones. Se puede dejar como una tabla resumen aparte (ver §3) o como badge al final del nombre del tema.
- Los nombres de carpeta son inconsistentes (`sesion-magistral_1`, `sesion_magistral-2`, `sesion_magistral_3`, `sesion_magistral-4`): conviene unificar a un solo patrón, p. ej. `sesion_magistral-N`, para que un script pueda recorrerlas sin casos especiales.

## 2. Cómo mantenerla organizada (estilo CS50)

CS50 funciona porque cada semana tiene una carpeta con una estructura *idéntica* (slides, notes, source, video) y una página de "Schedule" que es solo un índice que enlaza a esas carpetas — no un lugar donde se escribe prosa. La bitácora nunca se desincroniza del material porque el material *es* la fuente de verdad y el schedule se limita a apuntar a él.

Traducido a este repo:

**a) Una sola fuente de verdad por sesión.** Cada `sesion_magistral-N/README.md` debe tener siempre los mismos campos, en el mismo orden, idealmente como front matter o tabla fija al inicio:

```markdown
- **Fecha:** 10 ago 2026
- **Modalidad:** 💻 Virtual
- **Clase:** 2 — Método de Polya
- **Contenido cubierto:** método de Polya hasta pseudocódigo, con ejemplos en Python (Spyder)
- **Pendiente para la próxima:** —
- **Material:** [diapositivas](../teoria/clase-02.pdf) · [código](./codigo/)
```

La tabla en `clases/README.md` deja de ser el lugar donde se escribe el detalle; se vuelve un **índice generado** a partir de estos archivos.

**b) Ritual de actualización, no acumulación.** El README de la sesión se llena el mismo día de clase o al día siguiente (mientras el recuerdo está fresco), como un commit de bitácora — no se deja para "poner todo al final del corte". Sugerencia de flujo:
1. Al terminar la clase, crear/editar `clases/N/sesion_magistral-M/README.md` con la plantilla de arriba.
2. Commit inmediato: `docs(clase-N): bitácora sesión M — dd mmm`.
3. Correr un script (ver c) que regenera la tabla fusionada de `clases/README.md` a partir de todas las plantillas.

**c) Automatizar la tabla fusionada.** Con nombres de carpeta consistentes y front matter fijo, un script corto (Python o Node, ~40 líneas) puede recorrer `clases/*/sesion_magistral-*/README.md`, extraer los campos y regenerar la tabla de `clases/README.md` completa cada vez. Esto elimina el riesgo de que el índice y la bitácora se desincronicen (que es justo el problema que están teniendo hoy: dos tablas mantenidas a mano). Puedo dejarles armado ese script si quieren.

**d) Estados explícitos por sesión, no solo por tema.** Añadir un estado por fila (`✅ Completo` / `🚧 Parcial` / `⏳ Pendiente detalle`) hace visible de un vistazo qué bitácoras faltan por completar — como la nota "*pendiente completar detalle de lo dicho*" que ya tienen para la sesión 6, pero de forma consistente en todas las filas.

**e) Reprogramaciones y festivos como parte del registro, no como nota suelta al final.** Ya lo están haciendo bien con la nota del 17 de agosto; sugiero moverlo a la celda de **Fecha** de la fila afectada (como en la tabla de arriba) para que quede junto al dato, en vez de en una nota aparte que hay que ir a buscar.

## 3. Tabla resumen por tema (opcional, separada)

Si quieren conservar una vista "por tema" además de la cronológica (útil para navegación rápida), se deriva automáticamente contando cuántas sesiones tiene cada Clase y si todas están completas:

| Clase | Tema | Sesiones | Estado |
|---|---|---|---|
| 0 | Presentación del curso | 1/1 | ✅ Completo |
| 1 | Conociendo las Herramientas de Trabajo | 1/1 | ✅ Completo |
| 2 | Método de Polya / lógica de resolución de problemas | 3/3 | ✅ Completo |
| 3 | Estructuras de control y ejemplos de código | 1/2+ (en curso) | 🚧 En curso |
| 4 | Por definir | 0 | ⏳ Pendiente |

Esta tabla queda arriba de la fusionada, para navegación rápida por tema, y la fusionada abajo como bitácora cronológica detallada — reemplazando las dos tablas actuales por una jerarquía de dos niveles en vez de dos tablas independientes que hay que sincronizar a mano.