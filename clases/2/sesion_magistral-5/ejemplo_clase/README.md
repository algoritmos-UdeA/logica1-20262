![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Ejemplo de clase — Método de Polya: Cálculo de nómina

Este directorio contiene un ejemplo completo y autocontenido de aplicación del **método de Polya** para resolver un problema de programación: calcular el salario neto de un empleado a partir de las horas trabajadas, el valor de la hora, y los descuentos de salud y pensión.

El objetivo es que cualquier estudiante pueda recorrer, de forma independiente, todo el proceso de solución: desde el análisis del enunciado hasta la implementación en Python y su verificación con casos de prueba.

## Punto de partida

Empieza por [`nomina_polya.md`](nomina_polya.md). Es el documento principal: contiene la plantilla del método de Polya completamente diligenciada (entender el problema, diseñar un plan, implementarlo y revisarlo), e incluye o enlaza a todos los demás archivos de esta carpeta en el punto donde son relevantes.

## Contenido del directorio

| Archivo | Descripción |
|---|---|
| [`nomina_polya.md`](nomina_polya.md) | Documento principal. Plantilla del método de Polya diligenciada para el problema de cálculo de nómina: enunciado, identificación de datos de entrada/salida/auxiliares, fórmulas, diagrama entrada-proceso-salida, pseudocódigo, diagrama de flujo, código Python y pruebas de escritorio con dos casos. |
| [`nomina.py`](nomina.py) | Solución en Python: pide por teclado el nombre, la identificación, las horas trabajadas y el valor por hora; calcula el salario neto descontando 10% de salud y 5% de pensión; e imprime un recibo de pago formateado en consola. Se puede ejecutar directamente con `python nomina.py`. |
| [`diagrama.png`](diagrama.png) | Diagrama de flujo del algoritmo (entrada → proceso → salida), correspondiente al paso "Implementar el plan" del método de Polya. |
| [`metodo_polya_nomina.pdf`](metodo_polya_nomina.pdf) | La plantilla oficial del método de Polya (formato PDF) ya diligenciada para este ejercicio — versión "en limpio" equivalente a `nomina_polya.md`. |
| [`metodo_polya_nomina_manuscrito.pdf`](metodo_polya_nomina_manuscrito.pdf) | Versión manuscrita de la solución, tal como se resolvió en clase a mano antes de pasarla a la plantilla digital. |
| [`test1.png`](test1.png) | Captura de pantalla de la ejecución del programa con el caso de prueba 1 (nombre: Bryan, 100 horas, $2000/hora). |
| [`test2.png`](test2.png) | Captura de pantalla de la ejecución del programa con el caso de prueba 2 (nombre: Marcos, 9.5 horas, $1500/hora). |

## Cómo estudiar este ejemplo

1. Lee el enunciado del problema y la sección "1. Entender el problema" en `nomina_polya.md`.
2. Revisa el plan (sección 2) y compáralo con el diagrama entrada-proceso-salida.
3. Sigue la implementación (sección 3): pseudocódigo, diagrama de flujo (`diagrama.png`) y código Python.
4. Ejecuta `nomina.py` con los mismos valores de los casos de prueba y compara tu salida con `test1.png` y `test2.png`.
5. Revisa las pruebas de escritorio (sección 4) para verificar manualmente los cálculos antes de correr el programa.
6. Si quieres ver la solución paso a paso sin instalar nada, usa el enlace a Python Tutor incluido en `nomina_polya.md`.

Para consultar cómo se resolvió el problema a mano, antes de pasarlo a la plantilla, revisa `metodo_polya_nomina_manuscrito.pdf`.

> [!Important]
> Se usó IA generativa para redactar y organizar este contenido a partir de indicaciones del docente. El docente revisó y validó la versión final.