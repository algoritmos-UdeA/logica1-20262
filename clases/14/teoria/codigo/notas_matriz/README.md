![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Notas finales de un curso con una matriz

## Qué hace

> Se tienen los nombres de los estudiantes de un curso y sus notas en tres parciales, que valen 30 %, 30 % y 40 %. Calcular la nota final de cada estudiante y mostrar quiénes obtuvieron la nota final más alta y quiénes la más baja.

Es el problema integrador de la [clase 14](../../../README.md) (diapositivas 42 a 49). Las notas se guardan en una **matriz**, con una fila por estudiante y una columna por parcial. Los nombres van en un arreglo paralelo a las **filas** y los pesos en un arreglo paralelo a las **columnas**. Si hay empate en la nota más alta o en la más baja, se muestran todos los estudiantes empatados.

Para verlo construido función por función: notebook [Notas finales de un curso con una matriz, paso a paso](../../notebooks/notas_finales_paso_a_paso.ipynb).

## Los archivos

```
📁 notas_matriz/
   📄 notas.py — las funciones, cada una con su especificación
   📄 test_notas.py — las pruebas con assert
   📄 main.py — el programa principal: def main() y la guarda
```

| Archivo | Contenido |
|---|---|
| [notas.py](notas.py) | `leer_nombres`, `leer_notas` (con `input()`), `calcular_notas_finales`, `buscar_mayor`, `buscar_menor`, `contar_iguales`, `posiciones_iguales` y `mostrar_estudiantes` |
| [test_notas.py](test_notas.py) | Pruebas de las funciones que calculan, incluido un empate. Las que usan `input()` o `print()` se prueban ejecutando el programa |
| [main.py](main.py) | Pide la cantidad de estudiantes (debe ser mayor que 0), los nombres y las notas, y muestra el resultado. `PESOS = [0.3, 0.3, 0.4]` es una constante |

`test_notas.py` y `main.py` hacen `import notas`: los tres archivos deben estar en la misma carpeta.

## Cómo ejecutarlo

Desde una terminal (o la de Anaconda), en esta carpeta:

```
cd clases/14/teoria/codigo/notas_matriz
python test_notas.py
python main.py
```

En Spyder: abra cada archivo y ejecútelo con **F5**.

## Salida esperada

Las pruebas:

```
Pruebas de notas: todas pasaron
```

El programa, con los datos de la clase. Primero se escribió una cantidad inválida (0):

```
Notas finales del curso
Cantidad de estudiantes: 0
ERROR: la cantidad debe ser mayor que 0
Cantidad de estudiantes: 4
Nombre del estudiante 1: Ana
Nombre del estudiante 2: Beto
Nombre del estudiante 3: Carla
Nombre del estudiante 4: Dario
Estudiante 1, parcial 1: 3.0
Estudiante 1, parcial 2: 3.5
Estudiante 1, parcial 3: 2.5
Estudiante 2, parcial 1: 4.5
Estudiante 2, parcial 2: 4.0
Estudiante 2, parcial 3: 5.0
Estudiante 3, parcial 1: 2.0
Estudiante 3, parcial 2: 3.0
Estudiante 3, parcial 3: 3.5
Estudiante 4, parcial 1: 4.0
Estudiante 4, parcial 2: 4.5
Estudiante 4, parcial 3: 3.0
Ana: 2.95
Beto: 4.55
Carla: 2.90
Dario: 3.75
Nota final mas alta: 4.55
  Beto
Nota final mas baja: 2.90
  Carla
```

## Si algo falla

| Lo que pasa | Por qué | Qué hacer |
|---|---|---|
| `ModuleNotFoundError: No module named 'notas'` | Se ejecutó desde otra carpeta, o `notas.py` no está junto a `main.py` | Entrar a la carpeta `notas_matriz` antes de ejecutar |
| `ValueError: could not convert string to float` | Se escribió una nota con coma (`3,5`) o con letras | Escribir las notas con punto: `3.5` |
| Las notas finales no coinciden con las de arriba | Se escribieron las notas en otro orden | Las notas se piden por estudiante: primero los tres parciales de Ana, después los de Beto |

> [!Important]
> Se usó IA generativa para redactar esta guía a partir del código de la clase. Las salidas son de ejecuciones reales. El docente revisa y valida la versión final.
