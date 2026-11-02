# Mejoras para la próxima versión del curso

Notas para preparar la siguiente versión de Lógica y Representación I. Salen de una autoevaluación del uso de IA generativa en la preparación del material, hecha el 2 de noviembre de 2026 con varios marcos de referencia internacionales, y de los pendientes que quedaron abiertos en el semestre 2026-2.

## 1. Uso de IA generativa en el curso

### Autoevaluación (2026-11-02)

| Marco | Puntaje (0-100) | Fortaleza | Vacío principal |
|---|---|---|---|
| Anthropic, *AI Fluency* (4D: delegación, descripción, discernimiento, diligencia) | ≈ 80 | Delegación y diligencia (85): el docente conserva las decisiones pedagógicas; transparencia en todo el material | Descripción y discernimiento (75): pedidos por partes; material publicado antes de la revisión del docente |
| UNESCO, *Marco de competencias en IA para docentes* (2024) y *Guía para la IA generativa en educación e investigación* (2023) | ≈ 82 | Mentalidad centrada en el ser humano, ética y desarrollo profesional (85) | Validar el contenido antes de usarlo con estudiantes; la IA no aparece en el aprendizaje del estudiante |
| MIT Teaching + Learning Lab, principios del Russell Group (2023) y política de IA de CS50 (Harvard) | ≈ 75 | Alineación con los objetivos de aprendizaje, equidad y acceso (Colab, Python Tutor) y buenas prácticas compartidas (90) | No hay una política escrita sobre cómo pueden usar la IA los estudiantes (35-40) |

Conclusión: el uso de la IA **por el docente**, para preparar material, está bien evaluado en todos los marcos. El vacío está en **el estudiante como usuario de IA**.

### Acciones recomendadas, de mayor a menor impacto

1. **Política de uso de IA para estudiantes.** Publicarla en el README principal o en la clase 0, con la estructura de la política de CS50 (Harvard):
   * **Usos razonables:** pedir que explique un concepto, que encuentre un error en el código propio, que sugiera casos de prueba, o comparar su explicación con una prueba de escritorio.
   * **Usos no razonables:** pedir la solución de un laboratorio, un taller o un parcial, o entregar código generado que no se entiende.
   * Qué se espera al entregar: declarar si se usó IA y para qué.
2. **Nota de transparencia de las sesiones.** Completarla con la frase que ya tienen los laboratorios: *"aun así, es posible que se haya pasado por alto algún error. Si encuentra alguna inconsistencia, se agradece informarla al docente para corregirla."* Así los estudiantes también revisan el material.
3. **Alfabetización en IA de los estudiantes.** Incluir al menos una actividad breve por unidad. Por ejemplo, pedirle a un asistente que explique un algoritmo (la búsqueda binaria, un ciclo) y buscar el error en su respuesta comparándola con la prueba de escritorio.
4. **Revisar antes de publicar.** Cuando no alcance el tiempo, publicar el material marcado como **"en revisión"** y quitar la marca después de leerlo completo. Así la nota "el docente revisó y validó la versión final" siempre es cierta.
5. **Pedidos completos al trabajar con IA.** Describir el entregable completo en un solo pedido, por ejemplo "notebook + README en cada carpeta + fila en las tablas + commit", con un referente concreto ("como la sesión 14"). Ahorra vueltas y da material más coherente.

## 2. Pendientes del semestre 2026-2

### Clase 11 (arreglos)

* Diapositiva 22: cambiar la frase "Antes y después: el mismo programa, mejor escrito." Las dos columnas muestran el mismo programa **con** el error, así que un estudiante puede leer la columna de Python como la corrección.
* Diapositiva 42: error de escritura, "La funcione recibe".
* Diapositiva 14: presenta `notas[-1]` como algo que el curso no usa, pero la convención actual sí lo permite, con la advertencia de que un índice negativo no da error. Esa advertencia no está en las diapositivas.
* Los docstrings de `recorrido_suma.py`, `indices_python.py` y `funciones_listas.py` citan la numeración de un plan anterior. Las diapositivas actuales son 15-21, 14/20/22 y 30-39, respectivamente.

### Clase 12 (ordenamiento y búsqueda)

* Correcciones de diapositivas que quedaron en espera:
  * **51:** la imagen tapa la viñeta del caso 3.
  * **34:** falta el árbol regenerado y el enlace de simulación.
  * **55:** hay que reescribir la tercera viñeta y agrandar el árbol.
  * **28:** `N - 1 - i` queda partido en dos líneas.
  * Ajustes de forma en los títulos y en el formato de las referencias.
* Volver a exportar `teoria/images/arbol_ordenamientos.png`: todavía dice "(bloque 3)".
* Enlaces de GitHub en las diapositivas de pruebas del integrador.

### Sesiones

* Sesión 29: enlazar la solución del Parcial 2 cuando esté disponible (`logica1_parcial2_2026-2-sol.pdf`).
* Sesiones 30 y 31 (03/11/2026): se documentaron como definitivas **antes** de dictarse. Hay que confirmar que el README y las filas de las tablas coinciden con lo que se vio en clase, y revisar los notebooks completos.
