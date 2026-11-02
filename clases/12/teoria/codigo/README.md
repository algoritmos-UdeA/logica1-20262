![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Clase 12 — Código de ejemplo

Esta carpeta reúne los programas de la clase 12, agrupados por **problema**. Cada sección presenta el enunciado y, debajo, los archivos que lo resuelven. Todos siguen la organización en archivos que se usa desde la [clase 10](../../../10/README.md): un módulo con las funciones, un archivo `test_<módulo>.py` con las pruebas, y un programa principal con `def main()` y la guarda `if __name__ == "__main__":`.

| # | Problema | Archivos | Diapositivas |
|---|---|---|---|
| 1 | [Buscar un valor en una lista](#1-buscar-un-valor-en-una-lista) | `busquedas.py` (`buscar_lineal`), `test_busquedas.py` | 11-16 |
| 2 | [Ordenar una lista](#2-ordenar-una-lista) | `ordenamientos.py`, `test_ordenamientos.py` | 17-35 |
| 3 | [Buscar en una lista ordenada](#3-buscar-en-una-lista-ordenada) | `busquedas.py` (`buscar_binaria`), `test_busquedas.py` | 36-43 |
| 4 | [Administración de notas de un curso](#4-administración-de-notas-de-un-curso) | Carpeta `curso/` | 44-57 |

> [!TIP]
> Las pruebas se ejecutan desde la carpeta de cada archivo, con `python test_busquedas.py`, `python test_ordenamientos.py` o, dentro de `curso/`, `python test_curso.py`. Si todas pasan, se imprime un único mensaje final; si alguna falla, el programa se detiene con `AssertionError` en la línea de esa prueba.

---

## 1. Buscar un valor en una lista

### Enunciado

> Dada una lista y un valor, encontrar la posición donde está el valor, o indicar que no está. La lista no necesita estar ordenada.

*(Enunciado redactado a partir de las diapositivas 11-15).*

La función retorna `-1` cuando el valor no está, porque ninguna posición válida es negativa. Con esa función se responde una de las preguntas del problema pendiente de la clase 11, **¿cuál es la nota de Carla?**: se busca `"Carla"` en `nombres` y la posición encontrada se usa en `notas` (diapositiva 15). Si el nombre no está, `pos` vale `-1` y no se debe usar `notas[pos]`: Python devolvería la última nota sin dar error, porque admite índices negativos.

### Archivos

| Archivo | Qué muestra |
|---|---|
| [busquedas.py](busquedas.py) | `buscar_lineal(lista, valor)`: recorre la lista desde la posición 0 y se detiene con `break` al encontrar el valor. Es del caso 1: retorna una posición y no modifica la lista. Al ejecutarlo, `main()` busca `3.5` en `[5.0, 4.0, 3.5, 2.87]` e imprime `2`. |
| [test_busquedas.py](test_busquedas.py) | Las pruebas de `buscar_lineal` (primera parte del archivo). |

### Casos de prueba

| Caso | Tipo | Resultado esperado |
|---|---|---|
| `3.5` en `[5.0, 4.0, 3.5, 2.87]` | Típico: está en el medio | `2` |
| `5.0` en la misma lista | Límite: es el primero | `0` |
| `2.87` en la misma lista | Límite: es el último | `3` |
| `7.0` en la misma lista | Especial: no está | `-1` |
| `1` en `[1, 2, 1]` | Especial: está repetido | `0` (la primera aparición) |
| `3.5` en `[]` | Especial: lista vacía | `-1` |

La función `contar_comparaciones_lineal` de la diapositiva 16, que cuenta cuántas comparaciones hace la búsqueda en el mejor y en el peor caso, no está en un archivo: se ejecuta desde el enlace de simulación de esa diapositiva.

---

## 2. Ordenar una lista

### Enunciado

> Ordenar una lista de menor a mayor **en el lugar**: la función recibe la lista, la deja ordenada y no retorna nada (caso 3). Se resuelve con tres métodos (selección, burbuja e inserción) que reutilizan funciones de apoyo.

*(Enunciado redactado a partir de las diapositivas 17-35).*

### Archivos

| Archivo | Qué muestra |
|---|---|
| [ordenamientos.py](ordenamientos.py) | Dos **funciones de apoyo**: `intercambiar(lista, i, j)`, que intercambia dos posiciones con una variable temporal `temp` (caso 3: MODIFICA la lista), y `posicion_menor(lista, inicio)`, que retorna la posición del menor desde `inicio` hasta el final (caso 1). Y los **tres métodos**: `ordenar_seleccion` (usa las dos funciones de apoyo), `ordenar_burbuja` (usa `intercambiar` y se detiene antes si una pasada no hizo intercambios) y `ordenar_insercion` (no usa ninguna: desplaza en vez de intercambiar). Al ejecutarlo, `main()` ordena `[29, 10, 14, 37, 13]` con los tres métodos y los tres imprimen `[10, 13, 14, 29, 37]`. |
| [test_ordenamientos.py](test_ordenamientos.py) | Las pruebas de las dos funciones de apoyo y de los tres métodos. Los tres métodos se prueban con los mismos cinco casos (el ejemplo de la clase, una lista ya ordenada, una al revés, una con repetidos y una de un solo elemento), dentro de un `for` que recorre las tres funciones. |

En las diapositivas, cada método aparece primero como un algoritmo suelto, con un `print` de depuración por pasada para ver cómo cambia la lista, y después como función. Esas versiones con traza se ejecutan desde los enlaces de simulación de las diapositivas 24, 28 y 31.

> [!WARNING]
> Como los métodos no retornan nada, se prueban en dos pasos: primero se llama a la función y después se revisa la lista con `assert`. Al final de `test_ordenamientos.py` hay una prueba comentada que muestra el error frecuente, `assert ordenar_seleccion(X) == [...]`: falla siempre, porque la función retorna `None`. Para verlo, basta quitar los `#` de esas dos líneas y ejecutar el archivo.

---

## 3. Buscar en una lista ordenada

### Enunciado

> Dada una lista **ordenada de menor a mayor** y un valor, encontrar una posición donde está el valor, o indicar que no está, descartando en cada paso la mitad de la lista que falta por revisar.

*(Enunciado redactado a partir de las diapositivas 36-40).*

### Archivos

| Archivo | Qué muestra |
|---|---|
| [busquedas.py](busquedas.py) | `buscar_binaria(lista, valor)`: usa `inicio`, `fin` y `medio = (inicio + fin) // 2`, con un `while` porque no se sabe de antemano cuántos pasos habrá. Que la lista esté ordenada es parte del *Supone*: la función no lo revisa, es responsabilidad de quien la llama. Al ejecutarlo, `main()` busca `15` en `[2, 5, 10, 12, 15, 17, 20]` e imprime `4`. |
| [test_busquedas.py](test_busquedas.py) | Las pruebas de `buscar_binaria` (segunda parte del archivo), todas con la lista `[2.87, 3.5, 4.0, 5.0]`, que es la de la búsqueda lineal ordenada. |

### Casos de prueba

| Caso | Tipo | Resultado esperado |
|---|---|---|
| `3.5` en `[2.87, 3.5, 4.0, 5.0]` | Típico: está en el medio | `1` |
| `2.87` en la misma lista | Límite: es el primero | `0` |
| `5.0` en la misma lista | Límite: es el último | `3` |
| `1.0` en la misma lista | Especial: menor que todos | `-1` |
| `7.0` en la misma lista | Especial: mayor que todos | `-1` |
| `3.7` en la misma lista | Especial: en un hueco | `-1` |
| `2` en `[1, 2, 2, 2, 3]` | Especial: está repetido | `2` (una de ellas, no necesariamente la primera) |
| `3.5` en `[]` | Especial: lista vacía | `-1` |

> [!WARNING]
> Al final de las pruebas de `buscar_binaria` hay una prueba comentada con la lista de mayor a menor, `[5.0, 4.0, 3.5, 2.87]`: no cumple el *Supone*, así que la función no encuentra el `3.5` aunque está en la lista. Al quitar el `#`, el archivo se detiene con `AssertionError` en esa línea.

---

## 4. Administración de notas de un curso

### Enunciado

> Un curso admite máximo N = 10 estudiantes. De cada uno se guarda su id (texto), su nombre y su nota. Por ahora hay 4 inscritos; se pueden agregar más hasta llenar el cupo. Se necesita un programa para administrar el curso: agregar, eliminar, actualizar, buscar, listar y ordenar.

*(Diapositiva 44).*

| Id | Nombre | Nota |
|---|---|---|
| `"000"` | `"Ana"` | `3.0` |
| `"123"` | `"Beto"` | `4.5` |
| `"987"` | `"Carla"` | `2.0` |
| `"007"` | `"Dario"` | `4.0` |
| *(libre)* | | |
| … | | |

El programa muestra un menú y se repite hasta que se elige `0. Salir`:

| Opción | Qué hace | Usa |
|---|---|---|
| 1. Agregar | Agrega al final si hay cupo y el Id no existe | `cantidad`, búsqueda lineal |
| 2. Eliminar | Quita un estudiante por Id y corre los siguientes a la izquierda | búsqueda lineal, desplazamiento |
| 3. Actualizar nota | Cambia la nota de un Id | búsqueda lineal |
| 4. Buscar | Muestra los datos de un Id | búsqueda lineal |
| 5. Listar | Muestra los inscritos | recorrido |
| 6. Ordenar por nota | De mayor a menor | selección + intercambio |
| 7. Ordenar por nombre | Alfabético | selección + intercambio |

*(Diapositivas 45-46).* En la clase se explican en detalle las opciones 6 y 7 (diapositivas 47-54); el resto del programa usa lo visto en clases anteriores.

### Archivos

La carpeta se ejecuta **desde su propia carpeta**: `python test_curso.py` y después `python main.py`.

| Archivo | Qué contiene |
|---|---|
| [curso/curso.py](curso/curso.py) | Las funciones del curso. Los estudiantes se guardan en tres **arreglos paralelos** de tamaño `N` (`ids`, `nombres` y `notas`), **parcialmente llenos**: solo las posiciones `0` a `cantidad - 1` tienen datos. Por eso las funciones reciben `cantidad` y recorren hasta ahí, no hasta `len()`, y las que cambian `cantidad` la retornan (`cantidad = agregar_estudiante(...)`). La pieza clave es `intercambiar_estudiantes`, que llama tres veces a `intercambiar`, una por arreglo, para mover al estudiante completo. `ordenar_por_nota` y `ordenar_por_nombre` son la selección con tres cambios: `posicion_mayor_nota` o `posicion_menor_nombre` en vez de `posicion_menor`, `cantidad` en vez de `len()` e `intercambiar_estudiantes` en vez de `intercambiar`. |
| [curso/test_curso.py](curso/test_curso.py) | Las pruebas de `curso.py`. Arma el curso de ejemplo con `agregar_estudiante` y usa una función auxiliar, `empieza_con`, que compara solo las posiciones ocupadas. Además de los casos típicos, prueba lo nuevo de este problema: que cada estudiante conserve su Id, nombre y nota al ordenar, que las casillas libres no se toquen, y que no se pueda agregar un Id repetido ni pasar del cupo. |
| [curso/main.py](curso/main.py) | El menú. Crea los tres arreglos con `[""] * N` y `[0.0] * N`, inscribe a los cuatro estudiantes del ejemplo y llama a una función de `curso.py` por cada opción. |
| [curso/ordenamientos.py](curso/ordenamientos.py) | Una copia de [ordenamientos.py](ordenamientos.py). Está ahí porque `curso.py` importa `intercambiar` con `from ordenamientos import intercambiar`, y Python solo encuentra el módulo si está en la misma carpeta. Si se cambia uno de los dos archivos, hay que cambiar también el otro. |

> [!NOTE]
> `ordenar_por_nombre` compara los nombres con `<`, que sigue el orden del diccionario solo si todos empiezan con mayúscula y no llevan tilde: `"ana" < "Beto"` y `"Álvaro" < "Beto"` dan `False`. Por eso esa condición está en el *Supone* de `posicion_menor_nombre`.

### Casos de prueba del programa principal

`main.py` no tiene pruebas automáticas; estos casos se prueban a mano, partiendo de los cuatro estudiantes iniciales.

| Opción | Entrada | Salida esperada |
|---|---|---|
| 5 | — | Ana, Beto, Carla y Dario, en el orden en que se inscribieron |
| 6 | — | Beto 4.5, Dario 4.0, Ana 3.0, Carla 2.0, cada uno con su Id |
| 7 | — | Ana, Beto, Carla, Dario, cada uno con su Id y su nota |
| 4 | Id `987` | `987 Carla 2.0` |
| 4 | Id `555` | `No existe un estudiante con ese Id.` |
| 1 | Id `123`, nombre `Otro`, nota `1.0` | `No se pudo agregar: el curso está lleno o el Id ya existe.` |
| 2 | Id `123` | `Estudiante eliminado.`; al listar quedan Ana, Carla y Dario |
| 9 | — | `Opción no válida.` |
| 0 | — | `Hasta luego.` |

---

> [!Important]
> Se usó IA generativa para redactar y organizar este contenido a partir del material de la clase. El docente revisó y validó la versión final.
