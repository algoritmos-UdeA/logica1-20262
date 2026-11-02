![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Paso 1 — Especificación y stubs

> Leer las notas de los estudiantes de un curso y mostrar el promedio, cuántas notas son mayores que el promedio y en qué posiciones están.

## Qué se pretende mostrar

1. **Primero el contrato, después el código.** Con el diseño top-down (diapositiva 41) se decidió qué funciones hacen falta. Dos ya existían y se **reutilizan** tal como se probaron en la Parte 2: `leer_notas` (Caso 2) y `calcular_promedio` (Caso 1). Las dos nuevas, `contar_mayores_que` y `posiciones_mayores_que`, ya tienen su **especificación** completa (*Supone / Garantiza*, diapositivas 42-43), pero todavía no están implementadas.
2. **Un stub permite ejecutar el programa antes de terminarlo.** Las dos funciones nuevas son *stubs*: retornan un valor fijo (`0` y `[]`), como en la clase 10. Con eso, `main.py` ya corre de principio a fin.
3. **Las pruebas dicen qué falta por hacer.** `test_notas.py` se escribió a partir de la especificación, antes de implementar las funciones. Al ejecutarlo, se detiene en la primera prueba que el stub no cumple.

| Archivo | Contenido |
|---|---|
| [`notas.py`](notas.py) | Las cinco funciones: dos reutilizadas (completas), dos nuevas (stubs) y `mostrar_resultados` |
| [`test_notas.py`](test_notas.py) | Las pruebas con `assert` de las cuatro funciones que no leen ni imprimen |
| [`main.py`](main.py) | El programa principal: valida que la cantidad sea mayor que 0 y llama a las funciones en el orden del árbol top-down (leer → calcular → buscar → mostrar) |

## Cómo ejecutarlo

Desde esta carpeta (`paso1_stubs/`), porque `test_notas.py` y `main.py` solo encuentran `notas.py` si están en la misma carpeta:

```
python test_notas.py
python main.py
```

## Salida esperada

### Las pruebas

```
Traceback (most recent call last):
  File "...\paso1_stubs\test_notas.py", line 16, in <module>
    assert notas.contar_mayores_que([3.0, 4.5, 2.0, 4.0], 3.375) == 2         # tipico
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError
```

Cómo leerlo:

* Las pruebas de `calcular_promedio` (líneas 11-13) pasaron: esa función ya estaba hecha.
* La línea 16 es la primera prueba de `contar_mayores_que`: con las notas de la clase y el promedio 3.375 debería retornar `2`, pero el stub retorna `0`.
* Python se detiene en la **primera** prueba que falla, así que las de `posiciones_mayores_que` todavía no se ejecutaron.

Observe que la línea 17, `contar_mayores_que([4.0, 4.0, 4.0], 4.0) == 0`, **pasaría** con el stub, porque el resultado esperado también es 0. Una prueba que pasa no demuestra que la función esté bien: por eso se prueban varios casos.

### El programa principal

Con 4 estudiantes y las notas 3.0, 4.5, 2.0 y 4.0:

```
Notas mayores que el promedio
Cantidad de estudiantes: 4
Nota del estudiante 1: 3.0
Nota del estudiante 2: 4.5
Nota del estudiante 3: 2.0
Nota del estudiante 4: 4.0
Promedio del curso: 3.38
Notas mayores que el promedio: 0
Posiciones: []
```

El programa **corre** sin errores, y el promedio ya es correcto, porque `calcular_promedio` está completa. Pero las dos últimas líneas están mal: deberían decir `2` y `[1, 3]`. El programa funciona por fuera, pero las pruebas muestran que todavía no está terminado.

## Siguiente paso

Implementar `contar_mayores_que` y `posiciones_mayores_que` hasta que `python test_notas.py` imprima `Pruebas de notas: todas pasaron`. La solución está en [`paso2_completo/`](../paso2_completo/).

> [!Important]
> Se usó IA generativa para preparar este material a partir de las diapositivas de la clase. El docente revisó y validó la versión final.
