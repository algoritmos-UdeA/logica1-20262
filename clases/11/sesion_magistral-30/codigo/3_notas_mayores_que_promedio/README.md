![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Parte 3 — Notas mayores que el promedio

> Leer las notas de los estudiantes de un curso y mostrar el promedio, cuántas notas son mayores que el promedio y en qué posiciones están.

Es el problema que quedó pendiente en la clase 10, resuelto con funciones y diseño top-down (diapositivas 40-47 de la [teoría de la clase 11](../../../teoria/README.md)). Ejemplo: con las notas 3.0, 4.5, 2.0 y 4.0, el promedio es 3.38 y hay 2 notas mayores, en las posiciones `[1, 3]`.

El programa se construye en dos pasos. Cada paso es una carpeta con los mismos tres archivos: `notas.py` (las funciones), `test_notas.py` (las pruebas) y `main.py` (el programa principal). De un paso al otro solo cambia `notas.py`.

| Carpeta | Qué se espera que el lector entienda | Qué pasa al ejecutarlo |
|---|---|---|
| [`paso1_stubs/`](paso1_stubs/) | Cómo se arma un programa **antes** de implementar todas sus funciones. Las funciones reutilizadas (`leer_notas` y `calcular_promedio`) ya están completas. Las nuevas (`contar_mayores_que` y `posiciones_mayores_que`) tienen su especificación, el contrato, pero son *stubs* que retornan un valor fijo. Las pruebas se escriben a partir de la especificación y señalan qué falta por hacer | `test_notas.py` se detiene con `AssertionError` en la primera prueba de `contar_mayores_que`. `main.py` corre, pero muestra `0` notas mayores y `[]` |
| [`paso2_completo/`](paso2_completo/) | Cómo se implementan las dos funciones nuevas para cumplir el contrato: el patrón **contar** dentro de una función, y cómo devolver una **lista nueva sin `append`** (contar, crear `[0] * cantidad` y llenar con un segundo índice). También, que una función puede usar a otra y que `main()` se lee como el árbol top-down | `test_notas.py` imprime `Pruebas de notas: todas pasaron`. `main.py` muestra `3.38`, `2` y `[1, 3]` con las notas del ejemplo |

Se recomienda leerlos en orden: primero `paso1_stubs/` y, antes de abrir `paso2_completo/`, intentar implementar las dos funciones hasta que pasen las pruebas.

Cada carpeta tiene su propio README, con lo que muestra el código, cómo ejecutarlo y la salida esperada. Los archivos se ejecutan **desde su propia carpeta**, porque `test_notas.py` y `main.py` solo encuentran `notas.py` si está en la misma carpeta:

```
cd paso1_stubs
python test_notas.py
python main.py
```

> [!Important]
> Se usó IA generativa para preparar este material a partir de las diapositivas de la clase. El docente revisó y validó la versión final.
