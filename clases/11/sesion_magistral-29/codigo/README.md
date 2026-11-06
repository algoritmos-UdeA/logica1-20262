![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Código solución parcial 2

Scripts con la solución de los cuatro puntos del [Parcial 2](../logica1_parcial2_2026-2.pdf). La explicación completa (prueba de escritorio, tablas de variables y respuestas a las preguntas) está en la [solución en PDF](../logica1_parcial2_2026-2-sol.pdf).

Cada script se ejecuta desde esta carpeta con:

```
python <archivo>.py
```

## Punto 1: análisis de código

* [punto1_prueba_escritorio.py](./punto1_prueba_escritorio.py)

Es el código del parcial con dos contadores agregados (`cnt_line5` y `cnt_line13`) que cuentan cuántas veces se ejecutan las líneas 5 y 13. Sirve para verificar la prueba de escritorio hecha a mano. No pide datos; su salida es:

```
8 6 4 2 
-----
2
-----
+++++
Nunca llega
12 2 True 12
*************************************************
Resultados prueba de escritorio
Veces que se ejecuta la linea 5: 9
Veces que se ejecuta la linea 13: 6
*************************************************
```

> [!NOTE]
> Los números de línea de los comentarios (`# Linea 5`, `# Linea 13`) se refieren al código del enunciado, no a este archivo, que tiene líneas adicionales.

## Punto 2: ambulancia más cercana

* [punto2_ambulancias_forma1.py](./punto2_ambulancias_forma1.py): la distancia mínima se inicializa con un valor muy grande (`999999999`) antes del ciclo.
* [punto2_ambulancias_forma2.py](./punto2_ambulancias_forma2.py): la distancia mínima se inicializa dentro del ciclo con la primera ambulancia leída (`if i == 0`).

Son las mismas dos formas de inicializar un extremo vistas en la [sesión 20](../../../8/sesion_magistral-20/README.md) (nota máxima y mínima). Con los datos del ejemplo del enunciado (emergencia en `(3, 4)` y ambulancias en `(0, 0)`, `(5, 5)`, `(2, 3)` y `(10, 1)`), las dos formas imprimen:

```
Ambulancia más cercana: (2.0, 3.0)
Distancia: 1.4142135623730951
```

## Punto 3: serie

* [punto3_serie.py](./punto3_serie.py)

Usa contadores para los factores del denominador (`term_1`, `term_2`) y el exponente (`expo`), una bandera para el signo (`signo`) y un acumulador (`suma`, que empieza en `1`, el primer término). Por eso el ciclo da `N - 1` vueltas. Con `X = 1` y `N = 3`:

```
La suma de los primeros 3 términos es: 0.5833333333333334
```

## Punto 4: triángulo hueco

* [punto4_patron_asteriscos.py](./punto4_patron_asteriscos.py)

Usa dos contadores de espacios: los de afuera del triángulo (`num_espacios1`, disminuye en cada fila) y los de adentro (`num_espacios2`, aumenta en cada fila intermedia). La primera fila, las filas intermedias y la última fila se tratan con `if`-`elif`-`else`. Con `N = 6`:

```
     *
    **
   * *
  *  *
 *   *
******
```
