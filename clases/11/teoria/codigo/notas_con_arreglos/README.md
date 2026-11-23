![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Notas mayores que el promedio

## Qué hace

> Leer las notas de los estudiantes de un curso y mostrar el promedio, cuántas notas son mayores que el promedio y en qué posiciones están.

Es el problema que quedó pendiente en la clase 10 y que la [clase 11](../../../README.md) resuelve con un **arreglo** (diapositivas 40 a 47). Sin arreglo no se podía: el promedio solo se conoce después de leer todas las notas, y con una sola variable solo quedaba la última. Con el arreglo, las notas quedan guardadas y se recorren otra vez para compararlas.

Para verlo explicado en clase, en dos pasos (primero las funciones como *stubs* y después completas): [sesión magistral 30](../../../sesion_magistral-30/codigo/3_notas_mayores_que_promedio/README.md).

## Los archivos

```
📁 notas_con_arreglos/
   📄 notas.py — las funciones, cada una con su especificación
   📄 test_notas.py — las pruebas con assert
   📄 main.py — el programa principal: def main() y la guarda
```

| Archivo | Contenido |
|---|---|
| [notas.py](notas.py) | `leer_notas(n)` (con `input()`), `calcular_promedio`, `contar_mayores_que`, `posiciones_mayores_que` (sin `append`: cuenta, crea el arreglo del tamaño justo y lo llena) y `mostrar_resultados` |
| [test_notas.py](test_notas.py) | Pruebas de las funciones que calculan |
| [main.py](main.py) | Pide la cantidad de estudiantes (debe ser mayor que 0) y las notas, y muestra el resultado |

## Cómo ejecutarlo

```
cd clases/11/teoria/codigo/notas_con_arreglos
python test_notas.py
python main.py
```

## Salida esperada

Las pruebas:

```
Pruebas de notas: todas pasaron
```

El programa, con las notas de la clase. Primero se escribió una cantidad inválida (0):

```
Notas mayores que el promedio
Cantidad de estudiantes: 0
ERROR: la cantidad debe ser mayor que 0
Cantidad de estudiantes: 4
Nota del estudiante 1: 3.0
Nota del estudiante 2: 4.5
Nota del estudiante 3: 2.0
Nota del estudiante 4: 4.0
Promedio del curso: 3.38
Notas mayores que el promedio: 2
Posiciones: [1, 3]
```

Las posiciones empiezan en 0: la posición 1 es el estudiante 2 (4.5) y la posición 3 es el estudiante 4 (4.0).

## Si algo falla

| Lo que pasa | Por qué | Qué hacer |
|---|---|---|
| `ModuleNotFoundError: No module named 'notas'` | Se ejecutó desde otra carpeta | Entrar a la carpeta `notas_con_arreglos` antes de ejecutar |
| `ValueError: could not convert string to float` | Se escribió una nota con coma (`3,5`) o con letras | Escribir las notas con punto: `3.5` |
| "Posiciones" no coincide con el número del estudiante | Las posiciones del arreglo empiezan en 0 y los estudiantes en 1 | La posición `i` es el estudiante `i + 1` |

> [!Important]
> Se usó IA generativa para redactar esta guía a partir del código de la clase. Las salidas son de ejecuciones reales. El docente revisa y valida la versión final.
